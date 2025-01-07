import face_recognition
import cv2
import numpy as np
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = 'attendance.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            date TEXT,
            time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_attendance(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Check if already logged today
    date = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("SELECT * FROM attendance WHERE name = ? AND date = ?", (name, date))
    if cursor.fetchone() is None:
        # Log new entry
        time = datetime.now().strftime('%H:%M:%S')
        cursor.execute("INSERT INTO attendance (name, date, time) VALUES (?, ?, ?)", (name, date, time))
        conn.commit()
        print(f"[LOGGED] {name} at {time}")
    else:
        print(f"[ALREADY LOGGED] {name}")
    conn.close()

# Load known faces
known_face_encodings = []
known_face_names = []

# Add known faces (images should be preprocessed for better accuracy)
known_faces = {
    "Aharan_image.jpeg": "Aharan",
    "anas_image.jpg": "Anas"
}

for img_path, name in known_faces.items():
    image = face_recognition.load_image_file(img_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(name)

# Initialize camera
video_capture = cv2.VideoCapture(0)

# Initialize DB
init_db()

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Find closest match
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            log_attendance(name)

        # Display results on video
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Display the video
    cv2.imshow('Video', frame)

    # Break with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
