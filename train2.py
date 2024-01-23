from ultralytics import YOLO
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = YOLO('yolov8x.pt')

# Other imports and function definitions

def main():
    # Your existing code to start the training
    results = model.train(
    data = r'C:\Users\Owner\Downloads\rainbowsix\data.yaml',
    imgsz=640,
    epochs=300,
    batch=16,
    name='yolov8_rainbowsix'
    )



if __name__ == '__main__':  
    main()
