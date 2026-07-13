import numpy as np

def manual_box_filter(integral_image, kernel_size):

    rows, cols = integral_image.shape

    output = np.zeros((rows, cols), dtype=np.float32)

    radius = kernel_size // 2

    for row in range(rows):
        for col in range(cols):

            top = max(0, row - radius)
            left = max(0, col - radius)

            bottom = min(rows - 1, row + radius)
            right = min(cols - 1, col + radius)

            total = integral_image[bottom, right]

            if top > 0:
                total -= integral_image[top - 1, right]

            if left > 0:
                total -= integral_image[bottom, left - 1]

            if top > 0 and left > 0:
                total += integral_image[top - 1, left - 1]

            area = (bottom - top + 1) * (right - left + 1)

            output[row, col] = total / area

    return output