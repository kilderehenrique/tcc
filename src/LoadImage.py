import cv2


face_cascade = cv2.CascadeClassifier('/home/vinicius/visao_computacional/data/haarcascades/haarcascade_frontalface_default.xml')
# Open the webcam
cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

#mudar para rgb 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w , h) in faces: 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    
    # Display the resulting frame
    cv2.imshow('Webcam Live Video', frame)

    # Quit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy the window
cap.release()
cv2.destroyAllWindows()