from ultralytics import YOLO
model = YOLO('yolov8n.pt') # load a pretrained model (recommended for training)
model = YOLO('ultralytics/runs/detect/train_model/weights/best.pt')
model.predict('outputImages/result.jpg', save=True, imgsz=320, conf=0.2)

import os
# ocr
command = "python extract.py model='ultralytics/runs/detect/train_model/weights/best.pt' source='outputImages/result.jpg'"


os.system(command)

