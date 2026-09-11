import cv2
import numpy as np

# IMAGE BASICS
# Grayscale: one channel, usually 0 (black) to 255 (white).
# Color: three channels. OpenCV uses BGR (Blue, Green, Red).
# Full HD: 1920 pixels wide × 1080 pixels high.


# 1. READ AN IMAGE
# Load an image from a file.
img = cv2.imread("img/images1.jpg")

# Stop if the image could not be loaded.
if img is None:
    raise FileNotFoundError("Could not load img/images1.jpg")

# Images are stored as NumPy arrays.
print(type(img))
print(img.shape)  # (height, width, channels)


# 2. DISPLAY AN IMAGE
cv2.imshow("Original Image", img)
cv2.waitKey(0)  # Wait until any key is pressed.
cv2.destroyAllWindows()  # Close all image windows.


# 3. CONVERT TO GRAYSCALE
# Convert the BGR image into a single grayscale channel.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale Image", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 4. MODIFY COLOR CHANNELS
# Channel indexes: 0 = Blue, 1 = Green, 2 = Red.
img_no_green = img.copy()  # Keep the original image unchanged.
img_no_green[:, :, 1] = 0  # Remove green from every pixel.

cv2.imshow("Without Green", img_no_green)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5. RESIZE AN IMAGE
# Resize to (width, height). This can stretch the image.
img_resize = cv2.resize(img, (1000, 100))

cv2.imshow("Resized Image", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 6. FLIP AN IMAGE
# 0 = vertical flip, 1 = horizontal flip, -1 = both.
img_flip = cv2.flip(img, 0)

cv2.imshow("Flipped Image", img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 7. CROP AND SAVE AN IMAGE
# Slice using img[y_start:y_end, x_start:x_end].
# End indexes are excluded. Use coordinates within your image.
img_crop = img[100:300, 200:500]

if img_crop.size > 0:
    cv2.imshow("Cropped Image", img_crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the cropped image to a file.
    cv2.imwrite("fruits.png", img_crop)
else:
    print("Crop is empty. Choose coordinates inside the image.")


# 8. CREATE A BLANK IMAGE
# Create a black image: 512 high × 512 wide × 3 color channels.
# uint8 stores whole-number pixel values from 0 to 255.
canvas = np.zeros((512, 512, 3), dtype=np.uint8)


# 9. DRAW A RECTANGLE
# Points use (x, y) coordinates. Colors use BGR order.
# thickness=-1 fills the rectangle.
cv2.rectangle(
    canvas,
    pt1=(100, 100),
    pt2=(300, 300),
    color=(255, 0, 0),  # Blue.
    thickness=2,
)


# 10. ADD TEXT
# org sets the bottom-left position of the text.
cv2.putText(
    canvas,
    text="Hello, OpenCV!",
    org=(100, 400),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.8,
    color=(255, 255, 255),  # White.
    thickness=2,
    lineType=cv2.LINE_AA,  # Smooth text edges.
)

cv2.imshow("Drawing Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()