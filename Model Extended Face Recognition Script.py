import cv2
import dlib
import os

# Check if the shape predictor model file exists
model_path = "shape_predictor_68_face_landmarks.dat"
if not os.path.exists(model_path):
    print(f"Error: The model file '{model_path}' does not exist!")
    exit()

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Try 0, 1, 2 depending on your system

# Check if the camera was successfully opened
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()
else:
    print("Successfully opened the camera.")

# Initialize dlib's face detector and landmark predictor
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor(model_path)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was captured correctly
    if not ret:
        print("Failed to grab frame!")
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = hog_face_detector(gray)

    # For each face, detect landmarks
    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)

        # Draw circles on the first 16 facial landmarks
        for n in range(0, 32):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)

    # Display the frame with landmarks
    cv2.imshow("Face Landmarks", frame)

    # Wait for the 'Esc' key to be pressed to exit
    key = cv2.waitKey(1)
    if key == 27:  # 27 is the ASCII value for the Escape key
        break

# Release the video capture and close any open windows
cap.release()
cv2.destroyAllWindows()
