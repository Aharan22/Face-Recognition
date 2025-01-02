import sqlite3
import cv2
import face_recognition
import numpy as np

# Stage 1 Creating or connect to a database
def create_db():
    conn = sqlite3.connect('face_recognition.db')
    c = conn.cursor()
    
    # Create a table for storing user details and face encodings
    c.execute('''
              CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                name TEXT NOT NULL,
                                                face_encoding BLOB NOT NULL
                                                )
              ''')
              
    conn.commit()
    conn.close()
    
    
    # Stage 2 , Capture the Face
    
def capture_face():
    
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Loading Pre Trained Face - Detector 
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascades_frontalface_default.xml')
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 2)
            
            cv2.imshow('Face Capture', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


 # Stage 3 - Face Detection and Encoding
 
def get_face_encoding(image):
     # Convert the image to RGB (face_recognition works with RGB images)
   rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

   # Detect face locations in the image
   face_locations = face_recognition.face_locations(rgb_image)

   # Encode faces
   face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

   if len(face_encodings) > 0:
       return face_encodings[0] # Return the first  face encoding
   return None

 # Stage 4 Register the users  face
def register_face(name, face_encoding):
    #Connecting to Sqlite3 DataBase
    conn = sqlite3.connect('face_recognition.db')
    c = conn.cursor()
    
    
    # Inserting userface encoding into the database
    
    c.execute('''
         INSERT INTO users (name, face_encoding) VALUES (?, ?)
         ''', (name,face_encoding.tobytes())) # Converting to Bytes
         
    conn.commit()
    conn.close()
    
    
    print(f"User {name} registered successfully.")
    
    # Stage 5- Registering User Function
def register_user():
    
    name = input("Enter your Name: ")
    
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
   
    if ret:
        # Detect Face and Encode it 
        face_encoding = get_face_encoding(frame)
        
        if face_encoding is not None:
            # Register the Face with a Name
            register_face(name, face_encoding)
        else:
            print("NO FACE DETECTED. PLEASE TRY AGAIN")
            
            
    cap.release()
    cv2.destroyAllWindows()
    
    
    # Main Execution
if __name__ == "__main__":
    
    # Creating a database and tables  if they do not exist
    
    create_db()
    
    
    # Register the user 
    
    register_user()
    
         

        
        
              
              
              
              
     