'''
Author: Kaitlyn Clements 
KUID: 3072622
DATE: 01/31/22
LAB: lab2
Last modified: 01/31/22 
Purpose: obtain a numerator and a denominator from the user. Then, display the result of long division from the user. You may assume integers as input, but you must prevent the user from crashing the system if they want to divide by zero!
'''

numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))

if denominator == 0 :
	print ("Sorry, you may not divide by zero.")
else:
	print (numerator ,  " / " , denominator , " = " , numerator//denominator , " R " , numerator%denominator)