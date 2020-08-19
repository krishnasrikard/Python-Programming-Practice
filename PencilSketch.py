import cv2
import matplotlib.image as pimg
import matplotlib.pyplot as plt

# Reading Image
img = pimg.imread('Me.jpg')

# Image to GrayScale conversion
img_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Uswing bitwise_not to invert brightness of pixels so as to find edges.
img = cv2.bitwise_not(img_grayscale)

# Smoothening the Image
img = cv2.GaussianBlur(img,(201,201),sigmaX=0,sigmaY=0)

# Final Image
img = cv2.divide(img_grayscale,255-img, scale=256)
plt.imshow(img, cmap='gray')
plt.imsave('Sketch.png',img, cmap='gray')
plt.show()
