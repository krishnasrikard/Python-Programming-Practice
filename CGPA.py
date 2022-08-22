import numpy as np
import pandas as pd

df = pd.read_csv('CGPA.csv')

def EstimateCGPA(df,ConsiderAdditionals):
	Map = {'A+':10, 'A':10, 'A-':9, 'B':8, 'B-':7, 'C':6, 'C-':5, 'D':4}
	
	Credits = []
	Grades = []
	S_Grade_Credits = 0
	
	for i in df.index:
		if ConsiderAdditionals:
			if df["Grade"][i] != 'S':
				Credits.append(df["Credits"][i])
				Grades.append(Map[df["Grade"][i]])
			else:
				S_Grade_Credits += df["Credits"][i]
			print ((df["Course"][i], df["Credits"][i], df["Grade"][i]))
				
		elif df["Elective Type"][i] != 'Additional':
			if df["Grade"][i] != 'S' :
				Credits.append(df["Credits"][i])
				Grades.append(Map[df["Grade"][i]])
			else:
				S_Grade_Credits += df["Credits"][i]
			print ((df["Course"][i], df["Credits"][i], df["Grade"][i]))
				
	CGPA = (np.sum(np.multiply(Credits,Grades)))/(np.sum(Credits))
	return np.round(CGPA,decimals=2), np.sum(Credits) + S_Grade_Credits

CGPA, Credits = EstimateCGPA(df,False)
print ("CGPA = " + str(CGPA) + ", Credits = " + str(Credits))
