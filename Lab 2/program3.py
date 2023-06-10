'''
Author: Kaitlyn Clements
KUID: 3072622
Date: 01/31/22
Lab: lab2
Last Modified: 01/31/22 
Purpose: Open a restaurant selling 3 items. Ask user if they want items, prompt y/n, if y find out how many, user must not be allowed to order less than 0 of an item, if they do set oder amount to 0, ask for their age: anyone 55+ gets a 55% discount after tax, anyone 5- get all cake free and should not be taxed or included in order, Display cost per item, a subtotal, a tax amount, a discount amount, and a grand total. 
'''

print ("==========================")
print ("Welcome to the restaurant!")
print ("==========================")
print (" ")

#Cold Pasta
cold_pasta = input("Do you want cold pasta? (y/n) : ")

if cold_pasta=='y' or cold_pasta=='Y':
	cold_pasta_quantity = int(input("How many?: "))
else :
    cold_pasta_quantity = 0

if cold_pasta_quantity < 0 :
    cold_pasta_quantity = 0

#Grilled Cheese
grilled_cheese = input("Do you want grilled cheese? (y/n): ")

if grilled_cheese=='y' or grilled_cheese=='Y':
    grilled_cheese_quantity = int(input("How many?: "))
else:
    grilled_cheese_quantity = 0

if grilled_cheese_quantity < 0 :
    grilled_cheese_quantity = 0


#PIE
pie = input ("Do you want pie?: (y/n) ")

if pie=='y' or pie=='Y' :
    pie_quantity = int(input("How many?: "))
else:
    pie_quantity = 0

if pie_quantity < 0 :
    pie_quantity = 0

#COSTS
cold_pasta_cost = float(2.50)
grilled_cheese_cost = float(5.55)
pie_cost = float (3.00)
                             
#Discounts
user_age = int(input("How old are you?: "))

if user_age >= 55 :
    total_discount = float(.55)
else:
    total_discount = 0

if user_age <= 5 :
    pie_cost = float(0.00)


cold_pasta_total = cold_pasta_quantity*cold_pasta_cost
grilled_cheese_total = grilled_cheese_quantity*grilled_cheese_cost
pie_total = pie_quantity*pie_cost

subtotal = round((cold_pasta_total + grilled_cheese_total + pie_total) , 2)
tax = round (subtotal * .08 , 2)
Total = round (subtotal*1.08 , 2)

print ( cold_pasta_quantity , " Cold Pasta @ " , cold_pasta_cost , "==>" , cold_pasta_total)
print ( grilled_cheese_quantity , " Grilled Cheese @ " , grilled_cheese_cost , "==>" , grilled_cheese_total)
print ( pie_quantity , " Pie @ " , pie_cost , "==>" , pie_total)

print ( "Subtotal: $" , subtotal)

print ( "Tax: $" , tax)

print ( "Discount: $" , round ((total_discount*Total) , 2))

print ("===================================")

print ("Total: $" , round(subtotal+tax-(total_discount*subtotal) , 2))

print ("Please come again!")