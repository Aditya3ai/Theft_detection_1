import os
import shutil
from sklearn.model_selection import train_test_split
from PIL import Image, ImageSequence

def extract_frames_from_gif(input_folder, output_folder):
    # Check if input folder exists
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder '{input_folder}' not found. Please check the folder path.")
    
    os.makedirs(output_folder, exist_ok=True)
    
    for gif_file in os.listdir(input_folder):
        if gif_file.endswith(".gif"):
            gif_path = os.path.join(input_folder, gif_file)
            print(f"Extracting frames from: {gif_path}")
            
            # Open GIF file using PIL
            with Image.open(gif_path) as gif:
                for i, frame in enumerate(ImageSequence.Iterator(gif)):
                    # Convert the frame to RGB mode before saving as JPEG
                    rgb_frame = frame.convert("RGB")
                    # Save each frame as a .jpg image
                    frame_filename = f"{os.path.splitext(gif_file)[0]}_frame_{i}.jpg"
                    frame_path = os.path.join(output_folder, frame_filename)
                    rgb_frame.save(frame_path, 'JPEG')  # Save as JPG
                    print(f"Saved frame {i} to {frame_path}")

def split_dataset(images_folder, labels_folder, train_folder, val_folder, test_size=0.2):
    # Check if the input folder exists
    if not os.path.exists(images_folder):
        raise FileNotFoundError(f"Input folder '{images_folder}' not found. Please check the folder path.")
    
    # Create train/val folders if they don't exist
    os.makedirs(train_folder + "/images", exist_ok=True)
    os.makedirs(train_folder + "/labels", exist_ok=True)
    os.makedirs(val_folder + "/images", exist_ok=True)
    os.makedirs(val_folder + "/labels", exist_ok=True)
    
    images = [img for img in os.listdir(images_folder) if img.endswith(".jpg")]
    if len(images) == 0:
        raise ValueError(f"No images found in {images_folder}. Please check the folder and ensure there are .jpg images.")
    
    print(f"Images found: {images}")
    
    train_images, val_images = train_test_split(images, test_size=test_size, random_state=42)
    
    for image in train_images:
        shutil.copy(os.path.join(images_folder, image), os.path.join(train_folder + "/images", image))
        shutil.copy(os.path.join(labels_folder, os.path.splitext(image)[0] + ".txt"), os.path.join(train_folder + "/labels", os.path.splitext(image)[0] + ".txt"))
    
    for image in val_images:
        shutil.copy(os.path.join(images_folder, image), os.path.join(val_folder + "/images", image))
        shutil.copy(os.path.join(labels_folder, os.path.splitext(image)[0] + ".txt"), os.path.join(val_folder + "/labels", os.path.splitext(image)[0] + ".txt"))

if __name__ == "__main__":
    # Correct input folder path
    input_folder = "C:/Users/aditya/Desktop/theft_detetction/dataset/input"  # Update with correct path
    output_folder = "./dataset/extracted_frames/input_frames"
    images_folder = "./dataset/extracted_frames/input_frames"
    labels_folder = "./dataset/annotations/train"
    train_folder = "./dataset/train"
    val_folder = "./dataset/val"
    
    try:
        # First, extract frames from GIF files
        extract_frames_from_gif(input_folder, output_folder)
        
        # Then, split the dataset into train and validation sets
        split_dataset(images_folder, labels_folder, train_folder, val_folder)
        
        print("Dataset split successfully!")
    
    except Exception as e:
        print(f"Error: {e}")
