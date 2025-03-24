import numpy as np
import cv2

im1 = cv2.imread(r'MYPRJ\sample250227\fish.jpg',cv2.IMREAD_GRAYSCALE)

# im2= cv2.add(im1,50)
# im3 = im1 + 50
im2 = cv2.subtract(im1,50)
im3 = im1 - 50

cv2.imshow("fish", im1)
cv2.imshow("fish2", im2)
cv2.imshow("fish3", im3)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(im1.shape)