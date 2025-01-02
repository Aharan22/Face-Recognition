import cv2
# Importing the OpenCV library

image= cv2.imread('1.png')
print(image)

 
  #Reading the image using imread() function

  
h,w = image.shape[:2]

   
#Extracting the height and width of an image 

print("Height = {}, Width = {}".format(h,w))

    #Extracting Red Green Black Colour Value (RGB values) 
    #Initially we have to randomly Choose a Pixel
    #By passsing in 100,100 for height and width
(B, G, R) = image[200,100] 

# Displaying the Pixel Values
print("R = {}, G = {}, B = {}".format(R, G, B))

#We can also pass the channel to extract
# The value for a specific Channel
 
B = image[200, 100, 0]
print("B = {}".format(B))


# We will calculate the region of interest
# by slicing the pixels of the image
roi = image[100 : 500, 100 : 700]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

     


# We can also resize an image in Python using resize() function.
# resize() takes two parameteres , the image and the the dimensions

resize = cv2.resize(image, (250, 500))
cv2.imshow("Resized Image", resize)
cv2.waitKey(0) 


# Changing the aspect ratio
# Maintain aspect ratio
ratio = 800 / w

dim = (800, int(h * ratio))
# Resizing the image
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resized Image", resize_aspect)
cv2.waitKey(0)


# Copying the original image
output = image.copy()

# Adding the text using putText() function
text = cv2.putText(output, 'OpenCV Demo', (500, 550),
                cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
