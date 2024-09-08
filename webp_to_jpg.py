from PIL import Image
import os

def convert_all_webp_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".webp"):
            input_path = os.path.join(input_folder, filename)
            output_filename = filename.replace(".webp", ".jpg")
            output_path = os.path.join(output_folder, output_filename)

            with Image.open(input_path) as img:
                img = img.convert("RGB")
                img.save(output_path, "JPEG")
                print(f"Конвертировано: {filename} -> {output_filename}")

input_folder = "images"
output_folder = input_folder
convert_all_webp_to_jpg(input_folder, output_folder)