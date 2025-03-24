import numpy as np
import cv2

#300x400 크기의 BGR 컬러 이미지 생성( 검은색 )
im = np.zeros((300,400,3),np.uint8)

#초록색(G)채널을 255로 설정
#open cv 는 BGR(Blue-Gren-Red)순서 사용
im [:150,200:,0] = 255 #초로색 채널 조작 

cv2.imshow("title", im)
cv2.waitKey(0)
cv2.destroyAllWindows()