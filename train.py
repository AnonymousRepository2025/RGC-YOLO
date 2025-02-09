import warnings, os
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('C:/Users/zhang/Desktop/RGC-YOLO-V4-master/RGC-YOLO.yaml')

    model.train(data='C:/Users/zhang/Desktop/RGC-YOLO-V4-master/rice-data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=32,
                close_mosaic=0,
                workers=16, 
                optimizer='SGD', 

                project='runs/train',
                name='exp',
                )