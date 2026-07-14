import os
import cv2

from src.image_loader import load_image
from src.log_transform import apply_log_transform
from src.illumination import estimate_illumination
from src.reflectance import recover_reflectance
from src.normalization import normalize_image


def process_image(image_path, kernel_size=61):
    """
    Complete intrinsic reflectance recovery pipeline.
    """

    # -----------------------------
    # Create output folder
    # -----------------------------
    output_folder = "static/results"
    os.makedirs(output_folder, exist_ok=True)

    # -----------------------------
    # Load image
    # -----------------------------
    image = load_image(image_path)

    # -----------------------------
    # Log Transform
    # -----------------------------
    log_image = apply_log_transform(image)

    # -----------------------------
    # Estimate Illumination
    # -----------------------------
    illumination = estimate_illumination(
        log_image,
        kernel_size
    )

    # -----------------------------
    # Recover Reflectance
    # -----------------------------
    reflectance = recover_reflectance(
        log_image,
        illumination
    )

    reflectance = normalize_image(reflectance)

    # -----------------------------
    # Save outputs
    # -----------------------------
    log_path = os.path.join(
        output_folder,
        "log_image.png"
    )

    illumination_path = os.path.join(
        output_folder,
        "illumination.png"
    )

    reflectance_path = os.path.join(
        output_folder,
        "reflectance.png"
    )

    cv2.imwrite(
        log_path,
        ((log_image-log_image.min()) /
         (log_image.max()-log_image.min())*255).astype("uint8")
    )

    cv2.imwrite(
        illumination_path,
        ((illumination-illumination.min()) /
         (illumination.max()-illumination.min())*255).astype("uint8")
    )

    cv2.imwrite(
        reflectance_path,
        (reflectance*255).astype("uint8")
    )

    return {
    "input": image_path.replace("\\", "/"),
    "log": log_path,
    "illumination": illumination_path,
    "reflectance": reflectance_path,

    "shape": image.shape,
    "dtype": str(image.dtype),

    "input_min": round(float(image.min()), 4),
    "input_max": round(float(image.max()), 4),

    "log_min": round(float(log_image.min()), 4),
    "log_max": round(float(log_image.max()), 4),

    "reflectance_min": round(float(reflectance.min()), 4),
    "reflectance_max": round(float(reflectance.max()), 4),

    "kernel_size": kernel_size,
    "status": "Completed"
}