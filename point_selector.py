import cv2

class PointSelector:
    def __init__(self, img_path):
        self.img = self.create_window(img_path)
        self.points_list = [[]]
        self.current_points = self.points_list[0]

        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('image', self.click_event)
        cv2.resizeWindow('image', 1920, 1080)
        cv2.imshow('image', self.img)
        print("Click on the image to select points. Press the 'a' key to switch to new line. Press 'Enter' or close the window to exit the picking.")

    def create_window(self, img_path):
        img = cv2.imread(img_path)
        if img is None:
            print(f'Failed to load the image from the path: {img_path}')
            exit()
        return img

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.current_points.append((x, y))
            cv2.circle(self.img, (x, y), 3, (0, 0, 0), -1)
            cv2.imshow('image', self.img)

    def pick_points(self):
        while True:
            key = cv2.waitKey(1)
            if key == 13 or cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:
                break
            elif key == ord('a'):
                self.current_points = []
                self.points_list.append(self.current_points)
                print(f"Switched to line {len(self.points_list)}")
            elif key == ord('s'):
                break

    def run(self):
        self.pick_points()
        cv2.destroyAllWindows()

    def split_points(self):
        list_of_list1 = []
        list_of_list2 = []
        for i in self.points_list:
            list1 = []
            list2 = []
            for j in i:
                list1.append(j[0])
                list2.append(j[1])
            if (list1 != []):
                list_of_list1.append(list1)
                list_of_list2.append(list2)

        return (list_of_list1, list_of_list2)
        
