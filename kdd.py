import os

def train_yolov5(data_yaml_path, epochs=50):
    # Check if the YOLOv5 train.py exists
    if not os.path.isfile("yolov5/train.py"):
        raise FileNotFoundError("train.py not found in the yolov5 directory.")
    
    # Check if the data.yaml exists
    if not os.path.isfile(data_yaml_path):
        raise FileNotFoundError(f"{data_yaml_path} not found. Please provide the correct path to the data.yaml file.")
    
    # Construct the command to run YOLOv5 training
    command = f"python yolov5/train.py --img 640 --batch 16 --epochs {epochs} --data {data_yaml_path} --weights yolov5s.pt"
    print(f"Running command: {command}")  # Print the command for debugging
    os.system(command)

if __name__ == "__main__":
    # Specify the correct path to the data.yaml
    data_yaml_path = r"C:\Users\aditya\Desktop\theft_detetction\data.yml"
    
    try:
        train_yolov5(data_yaml_path)
        print("YOLOv5 training started!")
    except Exception as e:
        print(f"Error occurred: {e}")
