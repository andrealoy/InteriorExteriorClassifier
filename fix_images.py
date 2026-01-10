from pathlib import Path
import imghdr
import os 

data_dir = "data/"
image_exts = [".png", ".jpg", ".jpeg"]

img_type_accepted = ["bmp" , "gif", "jpeg", "png"]
for filepath in Path(data_dir).rglob("*"):
    if filepath.suffix.lower() in image_exts:
        img_type = imghdr.what(filepath)
        if img_type not in img_type_accepted:
            print(f"Deleting file: {filepath} of type: {img_type}")
            os.remove(filepath)
        else: 
            print(f"Accepted file: {filepath} of type: {img_type}")
            
print("Image fixing completed.")
