"""
Filename: init.py
Usage: This script will measure different objects in the frame using a reference object of known dimension. 
The object with known dimension must be the leftmost object.
"""
from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

# Function to show array of images (intermediate results)
def show_images(images):
	for i, img in enumerate(images):
		cv2.imshow("image_" + str(i), img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

img_path = "start2.jpeg"

# Read image and preprocess
image = cv2.imread(img_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9, 9), 0)

edged = cv2.Canny(blur, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

#show_images([blur, edged])

# Find contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Sort contours from left to right as leftmost contour is reference object
(cnts, _) = contours.sort_contours(cnts)

# Remove contours which are not large enough
cnts = [x for x in cnts if cv2.contourArea(x) > 100]

cv2.drawContours(image, cnts, -1, (0,255,0), 3)
# cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Resized_Window", 300, 700)
# cv2.imshow("Resized_Window", image)
# show_images([image, edged])
# print(len(cnts))
# print(cnts[0])

# Reference object dimensions
# Here for reference I have used a 2cm x 2cm square
if len(cnts)>0:
    ref_object = cnts[0]
    box = cv2.minAreaRect(ref_object)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    dist_in_pixel = euclidean(tl, tr)
    dist_in_cm = 2
    pixel_per_cm = dist_in_pixel/dist_in_cm

# Draw remaining contours
    for cnt in cnts:
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect
        object_width = w / pixel_per_cm
        object_height = h / pixel_per_cm
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)
        cv2.polylines(image, [box], True, (255, 0, 0), 2)
        # box = cv2.minAreaRect(cnt)
        # box = cv2.boxPoints(box)
        # box = np.array(box, dtype="int")
        # box = perspective.order_points(box)
        # (tl, tr, br, bl) = box
        # cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 2)
        # mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0])/2), tl[1] + int(abs(tr[1] - tl[1])/2))
        # mid_pt_verticle = (tr[0] + int(abs(tr[0] - br[0])/2), tr[1] + int(abs(tr[1] - br[1])/2))
        # wid = euclidean(tl, tr)/pixel_per_cm
        # ht = euclidean(tr, br)/pixel_per_cm
        # print(wid, ht, ";;")
        print(object_width, object_height)
        cv2.putText(image, "{:.1f}cm".format(object_width), (int(x-10), int(y-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        cv2.putText(image, "{:.1f}cm".format(object_height), (int(x-10), int(y+15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)


cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resized_Window", 450, 600)
cv2.imshow("Resized_Window", image)
show_images([image])