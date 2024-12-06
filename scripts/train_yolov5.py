import os

def train_yolov5(data_yaml_path, epochs=50):
    # Absolute path to train.py in yolov5 folder
    command = f"python C:/Users/aditya/Desktop/theft_detetction/yolov5/train.py --img 640 --batch 16 --epochs {epochs} --data {data_yaml_path} --weights yolov5s.pt"
    os.system(command)

if __name__ == "__main__":
    # Absolute path to data.yaml if needed
    train_yolov5(r"C:\Users\aditya\Desktop\theft_detetction\data.yml")
    print("YOLOv5 training started!")
