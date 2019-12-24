import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
import math
import PIL
from skimage.color import rgb2gray
import time

img1 = scipy.ndimage.imread('Right.jpeg')							
img1 = rgb2gray(img1)									

img2 = scipy.ndimage.imread('Left.jpeg')							
img2 = rgb2gray(img2)									

plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
plt.imshow(img1)
ax = plt.subplot(1,2,2)
plt.imshow(img2)
plt.show()

shape = np.shape(img1)

def Compatability(img1,img2,i,j,ds,sigma=1):
	
	shape = np.shape(img1)
	x = 1
	
	if (i+ds < shape[0] and j < shape[1]):
		x = img1[i][j] - img2[i][j];
		x = (x * (-0.5))/(sigma*sigma)
		x = math.exp(x)
	
	return x

def Neighborhood(ds,dt,gamma=2,delta=0.001):
	u, v = pow((ds - dt),2), pow(delta,2)
	m = min(u,v)
	m = -0.5 * m /(pow(gamma,2))
	m = math.exp(m)
	
	return m
	
def SumOver(img1,img2,i,j,ds,gamma=1,delta=0.001):
	dt = np.arange(1,11)
	s = np.zeros(10)
	for i in range(10):
		s[i] = Neighborhood(ds,dt[i]) * Compatability(img1,img2,i,j,dt[i])
	
	x = np.sum(s)
		
	return x

def Product(img1,img2,i,j,ds):
	x,y,p = i,j,1
	
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			if (i != x and j != y):
				p = p * SumOver(img1,img2,i,j,ds)
	
	p = p * Compatability(img1,img2,x,y,ds)	
	
	return p
	
def Maxi(img1,img2,i,j):
	
	ds = np.arange(1,11)
	r = np.zeros(10)
	
	for i in range(10):
		r[i] = Product(img1,img2,i,j,ds[i])
	
	x = np.argmax(r)
	
	return ds[x]		
				
	
def Image(img1,img2):
	shape = np.shape(img1)
	
	output = np.zeros(shape)
	
	for i in range(64,192):
		for j in range(64,192):
			output[i][j] = Maxi(img1,img2,i,j)
			print (i,j)
	
	return output

start = time.time()
m = Image(img1,img2)
end = time.time()
print (end-start)

plt.imshow(m)
plt.show()
	
