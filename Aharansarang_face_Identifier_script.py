import face_recognition
import cv2

#  Phase 1 - Load known images and generate their face encodings
known_image1 = face_recognition.load_image_file("Aharan_image.jpeg")
known_face_encoding1 = face_recognition.face_encodings(known_image1)[0]

known_image2 = face_recognition.load_image_file("sarang_image.jpeg")
known_face_encoding2 = face_recognition.face_encodings(known_image2)[0]

# List of known faces
known_faces = [known_face_encoding1, known_face_encoding2]

# Phase 2 
# Start Webcam Video Capture

video_capture = cv2.VideoCapture(0)


while True:
    # Capture a single frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(frame)

    # Get face encodings for each face in the frame
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for face_encoding in face_encodings:
        # Compare the detected face with the known faces
        results = face_recognition.compare_faces(known_faces, face_encoding)

        # If a match is found, display a message
        if True in results:
            print("Face matched!")
            # Draw a rectangle around the matched face
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, "Match Found", (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            print("No match found.")
            # Draw a rectangle around faces that do not match
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, "No Match", (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Webcam - Face Recognition", frame)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
#Releasing the webcam and Closing the Window
video_capture.release()
cv2.destroyAllWindows()

                
            

   
    
