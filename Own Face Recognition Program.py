import cv2
import face_recognition 
import numpy as np

# Initializing Use of Webcam
cap = cv2.VideoCapture(0)

# Loading Sample Image of Myself for Reference
my_image = face_recognition.load_image_file("Aharan_image.jpeg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]

# Creating an Array To Store Known Face encodings and names
known_face_encoding = [my_face_encoding]
known_face_names = ["Aharan"]

# Initializing Some Variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


    
if process_this_frame:
       # Finding all face locations and face encodings in the current frame
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        
        face_names = [] 
        for face_encoding in face_encodings:
            # Comparing this Face Encoding with the known face encodings
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            # If a match is found use name of the first match
            
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                
                
                face_names.append(name)
                
        process_this_frame = not process_this_frame
        
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_name):
            # Scale back up to the original size of the Image
            top *=4
            right *=4
            bottom *=4
            left *=4
            
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            
            # Label the face with a name
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, top - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image with the face identified
cv2.imshow('Face Recognition', frame)

    # Break the loop if 'q' is pressed
                                      if cv2.waitKey(1) & 0xFF == ord('q'):
                                         break

# Release the video capture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
            
             
    
    
