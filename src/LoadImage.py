import cv2
from matplotlib import pyplot as plt

# Load an image from the assets folder
image = cv2.imread('./assets/stopsign.jpg')

# Check if image loading was successful
if image is None:
    print('Could not open or find the image')
else:
    # Display the image in a window
    #cv2.imshow('image', image)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    stop_data = cv2.CascadeClassifier('./assets/stop_data.xml')
    found = stop_data.detectMultiScale(image_gray, minSize=(20,20))

    amount_found = len(found)

    if amount_found != 0: 
        for(x, y, width, height) in found:
            cv2.rectangle(image_rgb, (x, y),
                         (x + width, y + height), 
                         (0, 255, 0), 5)
            


    plt.subplot(1,1,1,)
    plt.imshow(image_rgb)
    plt.show()
  
  
    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()