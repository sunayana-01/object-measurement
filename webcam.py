# import cv2 as cv2
#
# url = 'http://192.168.222.58:8080/video'
# cap = cv2.VideoCapture(url)
#
# while True:
#     ret, frame = cap.read()
#     if frame is not None:
#         cv2.imshow('frame-captured', frame)
#     q = cv2.waitKey(1)
#     if q == ord('q'):
#         break
# cv2.destroyAllWindows()