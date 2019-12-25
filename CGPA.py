import numpy as np

n = int(input("Enter No.of Courses : "))

credit = np.zeros(n)
grade = np.zeros(n)

Map = {'A+':10, 'A':10, 'A-':9, 'B':8, 'B-':7, 'C':6, 'C-':5, 'D':4}

for i in range(n):
	
	credit[i] = int(input("Enter No.of Credits : "))
	grade[i] = Map[input("Enter Grade : ")]
	
CGPA = (np.sum(np.multiply(credit,grade)))/(np.sum(credit))

print (np.sum(np.multiply(credit,grade)))
print (np.sum(credit))
print (CGPA)
