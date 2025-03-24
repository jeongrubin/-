import numpy as np
import cv2

im1 = cv2.imread(r'MYPRJ\sample250227\lena_g.jpg',cv2.IMREAD_UNCHANGED)
im2 = cv2.imread(r'MYPRJ\sample250227\lena_g.jpg',cv2.IMREAD_GRAYSCALE)
im3 = cv2.imread(r'MYPRJ\sample250227\lena_g.jpg',cv2.IMREAD_COLOR)


print(im1.shape, im2.shape,im3.shape)
cv2.imshow("title1", im1)
cv2.imshow("title2", im2)
cv2.imshow("title3", im3)
cv2.waitKey(0)
cv2.destroyAllWindows()
