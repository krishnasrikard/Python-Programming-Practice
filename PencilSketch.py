import cv2
import matplotlib.image as pimg
import matplotlib.pyplot as plt

# Reading Image
cap = cv2.VideoCapture(0)
ret, img = cap.read()

# Image to GrayScale conversion
img_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Uswing bitwise_not to invert brightness of pixels so as to find edges.
img = cv2.bitwise_not(img_grayscale)

# Smoothening the Image
img = cv2.GaussianBlur(img,(201,201),sigmaX=0,sigmaY=0)

# Final Image
img = cv2.divide(img_grayscale,255-img, scale=256)
plt.figure(figsize=(10,10), dpi=200)
plt.imshow(img, cmap='gray')
plt.show()
