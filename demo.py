import cv2

# Load an image
img = cv2.imread('your_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray)

# Wait for a key press and close the window afterwards
cv2.waitKey(0)
cv2.destroyAllWindows()