import numpy as np

def normalize_image(image):
    """
    Normalize image into [0,1] and apply gamma correction
    only for visualization.
    """

    minimum = image.min()
    maximum = image.max()

    normalized = (image - minimum) / (maximum - minimum + 1e-8)

    # Visualization enhancement
    gamma = 0.6
    normalized = np.power(normalized, gamma)

    return normalized