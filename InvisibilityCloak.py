import warnings
warnings.filterwarnings("default", category=DeprecationWarning)
import cv2
import numpy as np
import time

capture = cv2.VideoCapture(0)
time.sleep(3)
for i in range(30):
	_,background = capture.read()

while(capture.isOpened()):
	_,img  = capture.read();
	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
	lower = np.array([0,0,0])
	upper = np.array([200,200,200])
	mask1 = cv2.inRange(hsv,lower,upper)
	
	lower = np.array([225,225,225])
	upper = np.array([255,255,255])
	mask2 = cv2.inRange(hsv,lower,upper)
	
	mask = mask1+mask2
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	img[np.where(mask==255)] = background[np.where(mask==255)]	
	
	cv2.imshow('Frame',img)
	cv2.waitKey(1)
