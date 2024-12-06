import os

def ensure_dir_exists(directory):
    os.makedirs(directory, exist_ok=True)

# Example
ensure_dir_exists('./dataset/extracted_frames/input_frames')
ensure_dir_exists('./dataset/extracted_frames/output_frames')
ensure_dir_exists('./dataset/annotations/train')
ensure_dir_exists('./dataset/annotations/val')
ensure_dir_exists('./dataset/train/images')
ensure_dir_exists('./dataset/train/labels')
ensure_dir_exists('./dataset/val/images')
ensure_dir_exists('./dataset/val/labels')
