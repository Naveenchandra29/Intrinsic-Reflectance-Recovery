import cv2
import numpy as np

from log_transform import apply_log_transform
from illumination import estimate_illumination
from reflectance import recover_reflectance
from normalization import normalize_image


def process_rgb_image(image_path, kernel_size=61):
    """
    Perform intrinsic reflectance recovery
    independently on the R, G and B channels.
    """

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError("Unable to load image.")

    image = image.astype(np.float32) / 255.0

    b_channel, g_channel, r_channel = cv2.split(image)

    recovered_channels = []

    for channel in [b_channel, g_channel, r_channel]:

        log_image = apply_log_transform(channel)

        illumination = estimate_illumination(
            log_image,
            kernel_size
        )

        reflectance = recover_reflectance(
            log_image,
            illumination
        )

        reflectance = normalize_image(reflectance)

        recovered_channels.append(reflectance)

    output = cv2.merge(recovered_channels)

    return image, output