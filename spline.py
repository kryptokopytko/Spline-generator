import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

class Spline:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def ini(self, x, y):
        n = len(x)
        h = np.zeros(n, dtype=np.float64)
        m = np.zeros(n, dtype=np.float64)

        for i in range(1, n):
            h[i] = x[i] - x[i - 1]

        lam = np.zeros(n, dtype=np.float64)
        for i in range(0, n - 1):
            lam[i] = h[i] / (h[i] + h[i + 1])

        f = np.zeros(shape=(n, 2), dtype=np.float64)
        for i in range(1, n):
            f[i, 0] = (y[i] - y[i - 1]) / (x[i] - x[i - 1])

        for i in range(2, n):
            f[i, 1] = (f[i, 0] - f[i - 1, 0]) / (x[i] - x[i - 2])

        u = np.zeros(n, dtype=np.float64)
        p = np.zeros(n, dtype=np.float64)
        q = np.zeros(n, dtype=np.float64)
        n -= 1
        for k in range(1, n):
            p[k] = lam[k] * q[k - 1] + 2
            q[k] = (lam[k] - 1) / p[k]
            u[k] = (6 * f[k + 1, 1] - lam[k] * u[k - 1]) / p[k]

        m[n - 1] = u[n - 1]
        for i in range(0, n - 2):
            k = n - 2 - i
            m[k] = u[k] + q[k] * m[k + 1]

        return m

    def s(self, k, arg, x, y, m, h):
        return 1 / h[k] * (1 / 6 * m[k - 1] * pow(x[k] - arg, 3) +
                           1 / 6 * m[k] * pow(arg - x[k - 1], 3) +
                           (y[k - 1] - 1 / 6 * m[k - 1] * h[k] * h[k]) * (x[k] - arg) +
                           (y[k] - 1 / 6 * m[k] * h[k] * h[k]) * (arg - x[k - 1]))

    def S(self, arg, x, y, n, m, h):
        for i in range(1, n):
            if (x[i - 1] <= arg <= x[i]):
                return self.s(i, arg, x, y, m, h)

    def plot_spline(self):
        plt.figure()
        for x, y in zip(self.X, self.Y):
            for i in range(0, len(y)):
                y[i] = -y[i]
            resx = np.arange(0, 1000, 0.1, dtype=np.float64)
            n = len(x)
            t = np.arange(0, n, dtype=np.float64)
            m = self.ini(t, x)
            h = np.zeros(n, dtype=np.float64)
            for j in range(1, n):
                h[j] = t[j] - t[j - 1]

            j = 0
            for i in resx:
                resx[j] = self.S(i, t, x, n, m, h)
                j += 1

            resy = np.arange(0, 1000, 0.1, dtype=np.float64)
            m = self.ini(t, y)
            j = 0
            for i in resy:
                resy[j] = self.S(i, t, y, n, m, h)
                j += 1

            plt.plot(resx, resy)

        ax = plt.gca()
        ax.set_aspect('equal', adjustable='box')
        plt.show()
