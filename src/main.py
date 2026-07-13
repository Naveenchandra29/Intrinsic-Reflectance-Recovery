from image_loader import load_image
import matplotlib.pyplot as plt

# Load the input image
image = load_image("../images/input/input.jpg")

# Display image information
print(f"Image Shape : {image.shape}")
print(f"Data Type   : {image.dtype}")
print(f"Minimum     : {image.min():.4f}")
print(f"Maximum     : {image.max():.4f}")

# Display image
plt.imshow(image, cmap="gray")
plt.title("Loaded Input Image")
plt.axis("off")
plt.show()