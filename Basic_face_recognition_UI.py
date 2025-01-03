import tkinter as tk
from tkinter import simpledialog,  messagebox
import cv2
import face_recognition
import os
import numpy as np

# Setting Up Directories for Storing Data
FACE_DB_DIR = "faces_db"
os.makedirs(FACE_DB_DIR, exist_ok=True)

    
# Function to Register a New Face And Associate it with a Name
def register_face():
    name = simpledialog.askstring("Register Face", "Enter your Name:")
    if not name:
        messagebox.showerror("Error", "Name cannot be empty!!")
        return
    
    cap = cv2.VideoCapture(0)
    messagebox.showinfo("Instructions", "Press 'Space' to capture your face, 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow("Register Face - Press 'space' to Capture", frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord(' '):
            face_locations = face_recognition.face_locations(frame)
            if len(face_locations) != 1:
                messagebox.showerror("Error", "Ensure only one face is visible in the frame!")
                continue
            face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
            
            # Saving the Face Encoding and Name
            np.save(os.path.join(FACE_DB_DIR, f"{name}.npy"), face_encoding)
            messagebox.showinfo("Success", f"Face for {name} registered successfully")
            break
        
        elif key == ord('q'): #To Quit 
            break
        
    cap.release()
    cv2.destroyAllWindows()
        
                                                                                 
 #Function to recognize Faces       
def recognize_face():
    # Loading all registered face encodings
    known_face_encodings = []
    known_face_names = []
    
    for file in os.listdir(FACE_DB_DIR):
        if file.endswith(".npy"):
            face_encoding = np.load(os.path.join(FACE_DB_DIR, file))
            known_face_encodings.append(face_encoding)
            known_face_names.append(file.split(".")[0])
            
            
    if not known_face_encodings:
        messagebox.showerror("Error", "No registered faces found!")
        return
    cap = cv2.VideoCapture(0)
    messagebox.showinfo("Instructions", "Press 'Q' TO quit.")
    
    
   
    
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        
        
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            #Use the known face with the smallest distance to the new face
            face_distances =  face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                
                # Drawing a rectangle around the face
           
                
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            
            cv2.putText(frame, name, (left + 6, bottom -  6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            
        cv2.imshow("Face Recognition", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    
# GUI Application Window

def main():
    root = tk.Tk()
    root.title("Aharans Face Registration and Recognition System")
    
    tk.Label(root, text="Face Registration and Recognition System", font=("Arial", 16)).pack(pady=10)
    
    tk.Button(root, text="Register your Face", command=register_face, font=("Arial", 14), bg="lightblue").pack(pady=10)
    tk.Button(root, text="Scan Face", command=recognize_face, font=("Arial", 14), bg="lightgreen").pack(pady=10)
    tk.Button(root, text="Exit", command=lambda: root.destroy(), font=("Arial", 14), bg="lightcoral").pack(pady=10)
    
    root.mainloop()
    
    
if __name__ == "__main__":
    main()
     
    
                                                                                              



        
     
      

    


        