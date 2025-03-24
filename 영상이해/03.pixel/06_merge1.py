import numpy as np
import cv2

im1 = cv2.imread(r'MYPRJ\sample250227\ground.png',cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread(r'MYPRJ\sample250227\tree2.png',cv2.IMREAD_GRAYSCALE)

#im3 = im1 + im2
im3 = cv2.addWeighted(im1, 0.4, im2, 0.6, 0)

cv2.imshow("title1", im1)
cv2.imshow("title2", im2)
cv2.imshow("title3", im3)
cv2.waitKey(0)
cv2.destroyAllWindows()