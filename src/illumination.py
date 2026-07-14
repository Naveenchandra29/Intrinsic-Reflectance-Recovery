from integral_image import compute_integral_image
from box_filter import manual_box_filter


def estimate_illumination(log_image, kernel_size=61):
   

    # Step 1: Compute the integral image
    integral = compute_integral_image(log_image)

    # Step 2: Estimate illumination using manual box filter
    illumination = manual_box_filter(integral, kernel_size)

    return illumination