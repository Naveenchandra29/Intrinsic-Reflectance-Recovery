import os
import cv2
import numpy as np

from src.log_transform import apply_log_transform
from src.illumination import estimate_illumination
from src.normalization import normalize_image


def process_rgb_image(image_path, kernel_size=61):
    """
    Recover intrinsic reflectance from an RGB image
    using a shared illumination map.
    """

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError("Unable to load image.")

    image = image.astype(np.float32) / 255.0

    # ------------------------------------
    # Estimate illumination from grayscale
    # ------------------------------------
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    log_gray = apply_log_transform(gray)

    illumination = estimate_illumination(
        log_gray,
        kernel_size
    )

    recovered_channels = []

    # ------------------------------------
    # Recover each RGB channel
    # ------------------------------------
    for channel in cv2.split(image):

        log_channel = apply_log_transform(channel)

        reflectance_log = log_channel - illumination

        reflectance = np.exp(reflectance_log)

        reflectance = normalize_image(reflectance)

        recovered_channels.append(reflectance)

    recovered_rgb = cv2.merge(recovered_channels)

    # Save RGB output
    output_path = "static/results/rgb_reflectance.png"

    cv2.imwrite(
        output_path,
        (recovered_rgb * 255).astype("uint8")
    )

    return {
        "original": image_path.replace("\\", "/"),
        "reflectance": output_path
    }