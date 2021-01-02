import numpy as np
import pandas as pd

df = pd.read_csv('CGPA.csv')

def EstimateCGPA(df,ConsiderAdditionals):
	Map = {'A+':10, 'A':10, 'A-':9, 'B':8, 'B-':7, 'C':6, 'C-':5, 'D':4}
	
	Credits = []
	Grades = []
	
	for i in df.index:
		if ConsiderAdditionals:
			if df["Grade"][i] != 'S':
				if df["Elective Type"][i] != 'Additional' or (df["Elective Type"][i] == 'Additional' and Map[df["Grade"][i]] > 8):
					print ((df["Course"][i], df["Elective Type"][i], df["Credits"][i], df["Grade"][i]))
					Credits.append(df["Credits"][i])
					Grades.append(Map[df["Grade"][i]])
		else:
			if df["Grade"][i] != 'S' and df["Elective Type"][i] != 'Additional':
				print ((df["Course"][i], df["Credits"][i], df["Grade"][i]))
				Credits.append(df["Credits"][i])
				Grades.append(Map[df["Grade"][i]])
				
	CGPA = (np.sum(np.multiply(Credits,Grades)))/(np.sum(Credits))
	
	return np.round(CGPA,decimals=2)

CGPA = EstimateCGPA(df,False)
print ("CGPA:",CGPA)
