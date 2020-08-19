import numpy as np
import pandas as pd

df = pd.read_csv('CGPA.csv')

courses = (df['Course'].to_numpy())
credit = (df['Credits'].to_numpy())
grade = (df['Grade'].to_numpy())

print (courses)

Map = {'A+':10, 'A':10, 'A-':9, 'B':8, 'B-':7, 'C':6, 'C-':5, 'D':4}

for i in range(grade.shape[0]):
	grade[i] = Map[grade[i]]
	
CGPA = (np.sum(np.multiply(credit,grade)))/(np.sum(credit))

print (np.sum(np.multiply(credit,grade)))
print (np.sum(credit))
print (np.round(CGPA,decimals=5))
