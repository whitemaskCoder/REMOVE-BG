from flask import Flask, render_template, request, redirect, url_for
from rembg import remove
from PIL import Image
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    images = os.listdir("static")
    output_images = [img for img in images if img.endswith(".png") and img.startswith("output_")]
    return render_template("index.html", output_images=output_images)

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist("images")
    os.makedirs("static", exist_ok=True)

    # Delete old output images
    for filename in os.listdir("static"):
        if filename.startswith("output_") and filename.endswith(".png"):
            os.remove(os.path.join("static", filename))

    # Process uploaded images
    for file in uploaded_files:
        input_image = Image.open(file)
        output_image = remove(input_image)
        output_filename = f"output_{uuid.uuid4().hex}.png"
        output_image.save(os.path.join("static", output_filename))

    return redirect(url_for("index"))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
