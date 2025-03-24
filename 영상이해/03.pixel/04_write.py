import numpy as np
import cv2

im = cv2.imread(r'MYPRJ\sample250227\lena_g.jpg',cv2.IMREAD_UNCHANGED)


cv2.imwrite(r'MYPRJ\sample250227\out2.jpg',im)
cv2.imshow("out1", im)
cv2.waitKey(0)
cv2.destroyAllWindows()