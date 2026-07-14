from flask import Flask, render_template, request
import os
import uuid
import time

from src.pipeline import process_image
from src.rgb_pipeline import process_rgb_image

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    if "image" not in request.files:
        return "No image uploaded."

    image = request.files["image"]

    if image.filename == "":
        return "Please select an image."

    # -------------------------
    # Kernel Size from UI
    # -------------------------
    kernel_size = int(request.form.get("kernel", 61))

    upload_folder = "static/uploads"
    os.makedirs(upload_folder, exist_ok=True)

    extension = os.path.splitext(image.filename)[1]

    filename = f"{uuid.uuid4().hex}{extension}"

    image_path = os.path.join(upload_folder, filename)

    image.save(image_path)

    start = time.time()

    results = process_image(
        image_path,
        kernel_size
    )

    rgb = process_rgb_image(
        image_path,
        kernel_size
    )

    end = time.time()

    processing_time = round(end - start, 3)

    return render_template(
        "results.html",
        results=results,
        rgb=rgb,
        processing_time=processing_time
    )


if __name__ == "__main__":
    app.run(debug=True)