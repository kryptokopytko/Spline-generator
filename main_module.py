# main_module.py
from spline import Spline
from point_selector import PointSelector
import numpy as np

def main():
    img_path = input("Enter filename (with path): ")
    point_selector = PointSelector(img_path)
    point_selector.run()

    # Access the selected points from PointSelector
    points_list = point_selector.split_points()

    # Example usage of SplineInterpolator
    spline_interpolator = Spline(points_list[0], points_list[1])
    spline_interpolator.plot_spline()

if __name__ == "__main__":
    main()
