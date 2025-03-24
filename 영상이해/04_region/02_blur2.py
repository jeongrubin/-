import numpy as np 
import cv2

im1 = cv2.imread('./sample/house.png',cv2.IMREAD_GRAYSCALE)

ker1 = np.array([1]*9, np.float32).reshape((3,3)) / 9
im2 = cv2.filter2D (im1,-1, ker1)

ker2 = np.array([1]*81, np.float32).reshape((9,9)) / 81
im3 = cv2.filter2D (im1,-1, ker2)

cv2.imshow("title1",im1)
cv2.imshow("title2",im2)
cv2.imshow("title3",im3)
cv2.waitKey(0)
cv2.destroyAllWindows()