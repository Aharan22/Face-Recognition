import cv2
import face_recognition
import pandas as pd
from datetime import datetime
import os

# Initialize Known Faces and names
known_face_encodings = []
known_face_names = []

# Mapping from the image filename to the person's name
name_mapping = {
    "Aharan_image": "Aharan",
    "anas_image": "Anas",
    "sarang_image": "Sarang"
}

# Function to load known faces
def load_known_faces(directory='known_faces/'):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Load the image file
            image_path = os.path.join(directory, filename)
            image = face_recognition.load_image_file(image_path)
            
            # Get face encodings from the image
            encodings = face_recognition.face_encodings(image)
            
            # If no face encoding is found, skip this image
            if not encodings:
                print(f"No faces detected in image: {filename}")
                continue  # Skip this image if no faces are detected
            
            encoding = encodings[0]  # Use the first face encoding (if there are multiple faces in an image)
            known_face_encodings.append(encoding)
            
            # Extract the name from the filename (without extension) and map it to the person's name
            name_key = filename.split('.')[0]  # e.g., "Aharan_image"
            name = name_mapping.get(name_key, "Unknown")  # Get the mapped name or "Unknown" if not found
            known_face_names.append(name)
            
            print(f"Loaded {filename} with encoding as {name}.")

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Initialize Attendance DataFrame
attendance_df = pd.DataFrame(columns=["Name", "Time"])

# Running the Video Capture Loop
face_locations = []
face_encodings = []
face_names = []

# Load known faces (ensure to load the dataset before starting video capture)
load_known_faces('known_faces/')

while True:
    ret, frame = video_capture.read()
    
    # Find all face locations and encodings in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    face_names = []

    # Debug: Print the number of faces detected in the current frame
    print(f"Detected {len(face_locations)} faces in the frame.")
    
    for face_encoding in face_encodings:
        # Check if the face matches known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
        name = "Unknown"
        
        print(f"Matches found: {matches}")  # Debugging line to see the match results

        # If a match is found, retrieve the name of the person
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        
        face_names.append(name)
        
        # Log attendance if the person is recognized and not already logged
        if name != "Unknown":
            # Check if the person is not already logged
            if not any(attendance_df['Name'] == name):
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Instead of append(), use pd.concat() to add a new row
                new_row = pd.DataFrame({"Name": [name], "Time": [current_time]})
                attendance_df = pd.concat([attendance_df, new_row], ignore_index=True)
    
    # Display the results on the frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Label the face
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    # Display the image with the recognized faces
    cv2.imshow('Video', frame)

    # Press 'q' to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()

# Save the attendance log to a CSV file
attendance_df.to_csv('attendance_log.csv', index=False)
