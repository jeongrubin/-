import numpy as np
import cv2

im = np.zeros((300,400),np.uint8)
im [:,:] = 0

cv2.imshow("title", im)
cv2.waitKey(0)
cv2.destroyAllWindows()