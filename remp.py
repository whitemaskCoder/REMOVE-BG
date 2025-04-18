from rembg import remove
from PIL import Image
import io

# === Input and Output paths ===
input_path = r'C:\Users\TUF\Documents\Python code\REMOVE-BG\REPOSITORY\photo_2023-03-17_10-04-10.jpg'   # Replace with your image path
output_path = 'output.png' # Output will have transparent background

# === Open and process image ===
with open(input_path, 'rb') as img_file:
    input_data = img_file.read()
    output_data = remove(input_data)  # Background removed

# === Save with original resolution and quality ===
output_image = Image.open(io.BytesIO(output_data))
output_image.save(output_path, format='PNG')

print("✅ Background removed and saved as:", output_path)
