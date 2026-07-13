import numpy as np
def apply_log_transform(image):
    """
    Convert the normalized image into the logarithmic domain.

    Parameters:
        image (numpy.ndarray): Input image with values in the range [0,1].

    Returns:
        numpy.ndarray: Log-transformed image.
    """

    # Small constant to avoid log(0)
    epsilon = 1e-6

    # Apply logarithmic transformation
    log_image = np.log(image + epsilon)

    return log_image