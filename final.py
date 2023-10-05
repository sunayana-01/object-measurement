import cv2
from object_detector import HomogeneousBgDetector
import numpy as np


img = cv2.imread('final3.jpeg')


detector = HomogeneousBgDetector()
contours = detector.detect_objects(img)
mina=999999
area=1
maxa=1
mina=area
minw=1
minh=1 
maxa=1 
maxw=1
maxh=1
        # Draw objects boundaries
for cnt in contours:
            # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect


    box = cv2.boxPoints(rect)
    box = np.intp(box)


    area=w*h
    x1 = w - h if w > h else h - w

    if (x1<=10) and area<mina:
        mina=area
        minw=w
        minh=h
    if area>maxa:
        maxa=area
        maxw=w
        maxh=h


    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {} cm".format(round(w, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Height {} cm".format(round(h, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)


scale=minw/5
maxw=maxw/scale
maxh=maxh/scale
print(maxw)
print(maxh)
cv2.imshow("Image", img)
cv2.waitKey(0)



cv2.destroyAllWindows()