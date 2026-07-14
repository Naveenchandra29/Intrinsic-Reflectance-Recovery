from image_loader import load_image
import matplotlib.pyplot as plt
import numpy as np
from log_transform import apply_log_transform
import cv2
from illumination import estimate_illumination
from reflectance import recover_reflectance
from normalization import normalize_image
from rgb_pipeline import process_rgb_image
# Load grayscale image
image = load_image("../images/input/input.jpg")

# Log transformation
log_image = apply_log_transform(image)

# Estimate illumination
illumination = estimate_illumination(log_image, kernel_size=61)

# Recover reflectance
reflectance = recover_reflectance(log_image, illumination)
print("\nReflectance Statistics")
print(f"Minimum : {reflectance.min():.6f}")
print(f"Maximum : {reflectance.max():.6f}")

# Normalize recovered reflectance
reflectance_normalized = normalize_image(reflectance)
cv2.imwrite(
    "../images/output/log_image.png",
    ((log_image - log_image.min()) /
     (log_image.max() - log_image.min()) * 255).astype("uint8")
)

cv2.imwrite(
    "../images/output/illumination_map.png",
    ((illumination - illumination.min()) /
     (illumination.max() - illumination.min()) * 255).astype("uint8")
)

cv2.imwrite(
    "../images/output/recovered_reflectance.png",
    (reflectance_normalized * 255).astype("uint8")
)

cv2.imwrite(
    "../images/output/recovered_reflectance.png",
    (reflectance_normalized * 255).astype("uint8")
)
# -----------------------------
# RGB Intrinsic Reflectance Recovery
# -----------------------------

original_rgb, recovered_rgb = process_rgb_image(
    "../images/input/input.jpg",
    kernel_size=61
)

cv2.imwrite(
    "../images/output/rgb_reflectance.png",
    (recovered_rgb * 255).astype("uint8")
)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].imshow(image, cmap="gray")
axes[0, 0].set_title("Input Image")
axes[0, 0].axis("off")
axes[0, 1].imshow(log_image, cmap="gray")
axes[0, 1].set_title("Log Image")
axes[0, 1].axis("off")
axes[1, 0].imshow(illumination, cmap="gray")
axes[1, 0].set_title("Estimated Illumination")
axes[1, 0].axis("off")
axes[1, 1].imshow(reflectance_normalized, cmap="gray")
axes[1, 1].set_title("Recovered Reflectance")
axes[1, 1].axis("off")
plt.tight_layout()
plt.show()
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(
    cv2.cvtColor(
        (original_rgb*255).astype(np.uint8),
        cv2.COLOR_BGR2RGB
    )
)
plt.title("Original RGB")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(
    cv2.cvtColor(
        (recovered_rgb*255).astype(np.uint8),
        cv2.COLOR_BGR2RGB
    )
)
plt.title("Recovered RGB Reflectance")
plt.axis("off")

plt.tight_layout()
plt.show()
# Display image information
print("\n----------- Image Information -----------")
print(f"Image Shape          : {image.shape}")
print(f"Image Data Type      : {image.dtype}")
print(f"Input Min Pixel      : {image.min():.4f}")
print(f"Input Max Pixel      : {image.max():.4f}")
print(f"Log Image Minimum    : {log_image.min():.4f}")
print(f"Log Image Maximum    : {log_image.max():.4f}")
print("\n----------- Processing Summary -----------")
print(f"Kernel Size           : 61")
print("Processing Pipeline   : Completed")
print("Recovered Reflectance : images/output/recovered_reflectance.png")
print("------------------------------------------")

