from PIL import Image
import os

# Input and Output folders
input_folder = "input"
output_folder = "output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Image file name
image_name = "sample.jpg.jpeg"

input_path = os.path.join(input_folder, image_name)
output_path = os.path.join(output_folder, "processed_image.jpg")

try:
    # Open image
    img = Image.open(input_path)
+
    # Resize image
    img = img.resize((400, 400))

    # Convert to grayscale
    img = img.convert("L")

    # Save processed image
    img.save(output_path)

    print("Image processed successfully!")
    print("Saved at:", output_path)

except FileNotFoundError:
    print("Error: sample.jpg not found in input folder.")
except Exception as e:
    print("Error:", e)