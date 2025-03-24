import numpy as np 
import cv2

im1 = cv2.imread('./sample/house.png',cv2.IMREAD_GRAYSCALE)
im2 = cv2.blur(im1,(3,3))
im3 = cv2.blur(im1,(9,9))

cv2.imshow("title1",im1)
cv2.imshow("title2",im2)
cv2.imshow("title3",im3)
cv2.waitKey(0)
cv2.destroyAllWindows()