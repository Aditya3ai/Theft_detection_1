import os
from PIL import Image

def extract_frames_from_gif(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through each GIF file in the input folder
    for gif_file in os.listdir(input_folder):
        if gif_file.endswith(".gif"):
            gif_path = os.path.join(input_folder, gif_file)
            gif = Image.open(gif_path)
            
            # Extract each frame from the GIF
            for frame_number in range(gif.n_frames):
                gif.seek(frame_number)
                frame = gif.convert("RGB")
                frame_path = os.path.join(output_folder, f"{os.path.splitext(gif_file)[0]}_frame{frame_number}.jpg")
                
                # Save the frame as an image
                frame.save(frame_path)
    
    print(f"Frames extracted successfully to {output_folder}")

if __name__ == "__main__":
    input_folder = "./dataset/extracted_frames/input_frames"
    output_folder = "./dataset/extracted_frames/output_frames"
    extract_frames_from_gif(input_folder, output_folder)
