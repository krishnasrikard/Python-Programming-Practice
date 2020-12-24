import numpy as np
import pandas as pd

df = pd.read_csv('CGPA.csv')

Courses = (df['Course'].to_numpy())
Credits = (df['Credits'].to_numpy())
Grades = (df['Grade'].to_numpy())

Map = {'A+':10, 'A':10, 'A-':9, 'B':8, 'B-':7, 'C':6, 'C-':5, 'D':4}

for i in range(Grades.shape[0]):
	Grades[i] = Map[Grades[i]]
	
CGPA = (np.sum(np.multiply(Credits,Grades)))/(np.sum(Credits))

print (np.sum(Credits))
print (np.round(CGPA,decimals=5))
