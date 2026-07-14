from flask import Flask, render_template, request
import os
import uuid

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

    # -----------------------------
    # Create upload folder
    # -----------------------------
    upload_folder = "static/uploads"
    os.makedirs(upload_folder, exist_ok=True)

    # -----------------------------
    # Create unique filename
    # -----------------------------
    extension = os.path.splitext(image.filename)[1]

    filename = f"{uuid.uuid4().hex}{extension}"

    image_path = os.path.join(upload_folder, filename)

    image.save(image_path)

    # -----------------------------
    # Run Grayscale Pipeline
    # -----------------------------
    results = process_image(image_path)

    # -----------------------------
    # Run RGB Pipeline
    # -----------------------------
    rgb_results = process_rgb_image(image_path)

    return render_template(
        "results.html",
        results=results,
        rgb=rgb_results
    )


if __name__ == "__main__":
    app.run(debug=True)