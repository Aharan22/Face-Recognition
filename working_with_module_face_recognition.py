import face_recognition

# Loading known images and generate their face encodings

known_image1 = face_recognition.load_image_file("sarang_image.jpeg")
known_face_encoding1 = face_recognition.face_encodings(known_image1)[0]

known_image2 = face_recognition.load_image_file("Aharan_image.jpeg")
known_face_encoding2 = face_recognition.face_encodings(known_image2)[0]

# Loading the image to recognize Faces From
image = face_recognition.load_image_file("version_old.jfif")

# Finding all the face locations in the uploaded image

face_locations = face_recognition.face_locations(image)

# Getting Face encodings for each face in the uploaded image

face_encodings = face_recognition.face_encodings(image, face_locations)

# Comparing the face encodings with known faces

known_faces = [known_face_encoding1, known_face_encoding2]

# Assuming the first detected face in the image is being compared

for face_encoding in face_encodings:
    results = face_recognition.compare_faces(known_faces, face_encoding)
    
    if True in results:
        print("MATCH FOUND")
    else:
        print("Faces Do Not Match!!!")
        
        


                                                       