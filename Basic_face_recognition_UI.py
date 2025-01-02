import tkinter as tk
from tkinter import simpledialog,  messagebox
import cv2
import face_recognition
import os
import numpy as np

# Setting Up Directories for Storing Data
if not os.path.exists("faces"):
    os.makedirs("faces")
if not os.path.exists("encodings"):
    os.makedirs("encodings")
    
    
#Creating Global Variables for storing Face Encodings And Names
known_face_encodings = []
known_face_names = []

# Function to Register a New Face And Associate it with a Name
def register_face():
    """Capture and register a face with a name."""
    def save_image_and_encoding(name, face_encoding):
        """Save the image and encoding to files."""
        face_file_path = f"faces/{name}.jpg"
        encoding_file_path = f"encodings/{name}.npy"
        
        ret, frame = cap.read()
        cv2.imwrite(face_file_path, frame)
        np.save(encoding_file_path, face_encoding)
        
        known_face_encodings.append(face_encoding)
        known_face_names.append(name)
        
        
        messagebox.showinfo("Registration Successful", f"Face of {name} registered successfully")
        
        
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect faces in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Draw rectangle around face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # Show the frame in the Tkinter window
        cv2.imshow("Register Face", frame)
        
        # Capture name from the user
        name = simpledialog.askstring("Name", "Enter your name:")
        if name:
            save_image_and_encoding(name, face_encodings[0])
            break
        
        # Break loop on pressing "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        
        cap.release()
        cv2.destroyAllWindows()
        
        
def recognize_face():
    """Recognize faces from webcam"""
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom -  6), font, 0.5, (255, 255, 255), 1)
            
            
        cv2.imshow("Face Recognition", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    
def start_registration():
    register_face()
    
    
def start_recognition():
    recognize_face()
    
root = tk.Tk()
root.title("Aharan's Face Registration and Recognition Application")

# Creating the UI Buttons

register_button = tk.Button(root, text="Register Face", command=start_registration, width=20, height=2)
register_button.pack(pady=20)

recognize_button = tk.Button(root, text="Recognize Face", command=start_recognition, width=20, height=2)
recognize_button.pack(pady=20)

#Starting the Tkinter event Loop
root.mainloop()



        
     
      

    


        
