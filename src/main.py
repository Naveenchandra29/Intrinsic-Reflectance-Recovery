from image_loader import load_image
import matplotlib.pyplot as plt
from log_transform import apply_log_transform
from integral_image import compute_integral_image

# Load the input image
image = load_image("../images/input/input.jpg")
# Apply logarithmic transformation
log_image = apply_log_transform(image)
# Compute Integral Image
integral = compute_integral_image(log_image)

# Display image information
print(f"Image Shape : {image.shape}")
print(f"Data Type   : {image.dtype}")
print(f"Minimum     : {image.min():.4f}")
print(f"Maximum     : {image.max():.4f}")
print(f"Log Image Minimum : {log_image.min():.4f}")
print(f"Log Image Maximum : {log_image.max():.4f}")
print("\nIntegral Image Information")
print(f"Shape       : {integral.shape}")
print(f"Data Type   : {integral.dtype}")
print(f"Minimum     : {integral.min():.4f}")
print(f"Maximum     : {integral.max():.4f}")

# Display image
plt.imshow(image, cmap="gray")
plt.title("Loaded Input Image")
plt.axis("off")
plt.show()
plt.figure(figsize=(6,6))
plt.imshow(log_image, cmap="gray")
plt.title("Log Transformed Image")
plt.axis("off")
plt.show()
plt.figure(figsize=(6,6))
plt.imshow(integral, cmap="gray")
plt.title("Integral Image")
plt.axis("off")
plt.show()