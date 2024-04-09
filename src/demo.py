import cv2

# Load an image from the assets folder
image = cv2.imread('./assets/EU.png')

# Check if image loading was successful
if image is None:
    print('Could not open or find the image')
else:
    # Display the image in a window
    cv2.imshow('image', image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()