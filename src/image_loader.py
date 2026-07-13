import cv2
import numpy as np
import os
def load_image(image_path):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image not found at: {image_path}"
        )
    # Read image in grayscale mode
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Check whether OpenCV loaded the image
    if image is None:
        raise ValueError(
            "Unable to read the image. Please check the file format."
        )
    # Convert image to float32
    image = image.astype(np.float32)
    # Normalize pixel values to [0,1]
    image = image / 255.0
    return image