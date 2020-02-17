# Code for proof of Central Limit Theorem

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.metrics import mean_squared_error

def Plot_Signal(x,y,i):
	# Plots a Signal
	if i>0:
		label = str(i) + "-fold Convolution of Signal"
	elif i==0:
		label = "Gaussian Signal"
	plt.title(label)
	plt.plot(x,y)
	plt.show()
	
def Central_Limit_Theorem(Signal,Time,n):
	# Outputs "n" times Convolved Signal restricted to a Maximum Value of 1.
	s = Signal.shape[0]
	for i in range(1,n+1):
		if i==1:
			Output = Signal
		else:
			Output = np.convolve(Output,Signal,'same')
			
		o = max(Output)
		Output = Output/o
		
	Plot_Signal(Time,Output,i)	
		
	return Output

Time = np.linspace(-2,2,1000,endpoint=True)
Signal = np.zeros(1000)
s = Signal.shape[0]
Signal[int(3*s/8):int(5*s/8)] = 1
# Signal obtained above describes a Benroulli Random Variable.

# No.of Convolutions Required
n = int(input("No.of Convolutions = "))

Central_Limit_Theorem(Signal,Time,n)
