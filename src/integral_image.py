import numpy as np

def compute_integral_image(image):
    """
    Compute the integral image manually.
    """

    rows, cols = image.shape

    integral_image = np.zeros((rows, cols), dtype=np.float32)

    for row in range(rows):
        for col in range(cols):

            current = image[row, col]

            top = integral_image[row - 1, col] if row > 0 else 0

            left = integral_image[row, col - 1] if col > 0 else 0

            top_left = (
                integral_image[row - 1, col - 1]
                if row > 0 and col > 0
                else 0
            )

            integral_image[row, col] = (
                current +
                top +
                left -
                top_left
            )

    return integral_image