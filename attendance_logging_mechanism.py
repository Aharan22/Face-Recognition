import cv2
import face_recognition
import pandas as pd
from datetime import datetime
import os
# Initialize Known Faces and names

known_face_encodings = []
known_face_names = []
def load_known_faces(directory='known_faces/'):
    
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            #Load the image file
            image_path = os.path.join(directory, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            
            if encodings:
                encoding = encodings[0]
                known_face_encodings.append(encoding)
                
            
          
               
                #Automatically extract name from the filename (before_image)
        base_name = filename.split('_')[0]
        known_face_names.append(base_name) # Adding the extracted name
           
           
          
# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Initializing  Attendance Data Frame

attendance_log = []

# Loading Known Faces Before Starting the video Capture

load_known_faces()

# Run Video Capture Loop

while True:
    ret, frame = video_capture.read()
    
    
    # Finding All Face Locations and encodings in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    face_names = []
    
    for face_encoding in face_encodings:
        # Checking if the face matches Known Faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        
        #If a match is found, retrieve the name of the person
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
             
        face_names.append(name)
        
        
        # Log Attendance if the person is recognized and not already logged
        if name !="Unknown" and not any(entry['Name'] == name for entry in attendance_log):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            attendance_log.append({"Name": name, "Time": current_time})
            
                
                 # Display the results
     
    for (top, right, bottom, left), name in zip(face_locations, face_names):
     # Choose the color based on whether the face is recognized or not
      if name != "Unknown":
         rectangle_color = (0, 255, 0)  # Green for recognized faces
      else:
         rectangle_color = (0, 0, 255)  # Red for unknown faces
     
     # Draw the rectangle around the face with the chosen color
      cv2.rectangle(frame, (left, top), (right, bottom), rectangle_color, 2)
     
     # Place the name near the face
      cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    # Display the image with the recognized faces
    
    cv2.imshow('Video', frame)

       # Exit Condition for the Loop (using Esc key)
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the Esc key
        break

                     

# Release the video capture object and close all windows

video_capture.release()
cv2.destroyAllWindows()

# Save the attendance log to a CSV file

attendance_df = pd.DataFrame(attendance_log)
attendance_df.to_csv('attendance_log.csv', index=False)
                                
                                    