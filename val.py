import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('runs/train/exp/weights/best.pt') 
    model.val(data='C:/Users/zhang/Desktop/RGC-YOLO-V4-master/rice-data.yaml',
              split='val', 
              imgsz=640,
              batch=16,

              project='runs/val',
              name='exp',
              )