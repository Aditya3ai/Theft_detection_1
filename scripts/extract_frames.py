import os
import cv2
from PIL import Image
import numpy as np

def extract_frames(gif_path):
    """
    Extract frames from a GIF file using PIL and return them as a list of frames.
    """
    try:
        gif = Image.open(gif_path)
        frames = []
        while True:
            # Convert the current frame to a numpy array
            frame = np.array(gif)
            frames.append(frame)
            try:
                # Move to the next frame
                gif.seek(gif.tell() + 1)
            except EOFError:
                break
        return frames
    except Exception as e:
        print(f"Error extracting frames from {gif_path}: {e}")
        return []

def save_frames(frames, output_path):
    """
    Save the extracted frames as individual images.
    """
    os.makedirs(output_path, exist_ok=True)
    for i, frame in enumerate(frames):
        frame_image = Image.fromarray(frame)
        frame_image.save(os.path.join(output_path, f"frame_{i+1}.png"))

def extract_frames_from_gif(input_folder, output_folder):
    """
    Extract frames from all GIFs in the input folder and save them in the output folder.
    """
    for gif_file in os.listdir(input_folder):
        if gif_file.endswith(".gif"):  # Ensure only .gif files are processed
            gif_path = os.path.join(input_folder, gif_file)
            frames = extract_frames(gif_path)
            if frames:
                output_path = os.path.join(output_folder, gif_file.split('.')[0])
                save_frames(frames, output_path)

    print("Frames extracted successfully!")

if __name__ == "__main__":
    input_folder = r'C:\Users\aditya\Desktop\theft_detetction\dataset\input'  # Update this with your actual path
    output_folder = r'C:\Users\aditya\Desktop\theft_detetction\dataset\extracted_frames\input_frames'  # Update this with your actual path

    extract_frames_from_gif(input_folder, output_folder)
