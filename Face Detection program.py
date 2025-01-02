import cv2
import dlib
 
cap = cv2.VideoCapture(0)

hog_face_detector = dlib.get_frontal_face_detector()

dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")



while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    print(ret, frame)
    
    # Checking if the frame was read correctly
    
    if not ret:
        print("Failed to Grab Frame!!!")
        break
    
    #Converting the frame to grayscale for Face Detection
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = hog_face_detector(gray)
    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)
        
        for n in range(0, 60):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            
            
    # Display the frame with landmarks
    cv2.imshow("Face Landmarks", frame)

    # Wait for the 'Esc' key to be pressed to exit
    key = cv2.waitKey(1)
    if key == 27:  # 27 is the ASCII value for the Escape key
        break

            
            

            
            


cap.release()
cv2.destroyAllWindows()
            