
# Intel OpenMP 런타임 라이브러리(libiomp5md.dll)가 이미 초기화된 상태에서 다시 초기화하려 할 때 발생하는 오류 해결
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    results = model(frame)
    for r in results:
        annotated_frame = r.plot()

    cv2.imshow("YOLOv8 Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()