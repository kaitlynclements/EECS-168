'''
Author: Kaitlyn Clements
KUID: 3072622
Date: 01/31/22
Lab: Lab 2
Last modified: 01/31/22
Purpose: write code to learn about what different categories of hurricane mean
'''

wind_speed = float(input("Enter a wind speed (m/s): "))

if wind_speed >= 70 :
	print ("A wind speed of " , wind_speed , " is a category 5 hurricane.")
elif 58 <= wind_speed < 70 :
	print ("A wind speed of " , wind_speed , " is a category 4 hurricane.")
elif 50 <= wind_speed < 58 : 
	print ("A wind speed of " , wind_speed , " is a category 3 hurricane.")
elif 43 <= wind_speed < 50 :
	print ("A wind speed of " , wind_speed , "is a category 2 hurricane.")
elif 33 <= wind_speed < 43 :
	print ("A wind speed of " , wind_speed , "is a category 1 hurricane.")
elif 18 <= wind_speed < 33 :
	print ("A wind speed of " , wind_speed , "is a tropical storm." )
elif 0 < wind_speed < 18 : 
	print ("A wind speed of " , wind_speed , "is a tropical depression.")
else : 
	print ("Invalid wind speed.")