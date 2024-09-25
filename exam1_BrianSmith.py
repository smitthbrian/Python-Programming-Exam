""""
Program: Paint Job Calculator
"""

# Author: Brian Smith
import math

#define constraints
door_area = 21
window_area = 7.5

#Prompt user for input
wall_length = float(input("Enter the wall length: "))
wall_height = float(input("Enter the wall height: "))
wall_count = float(input("Total number of walls with this dimension: "))

#Walls (sqft)
wall_area = wall_count * (wall_length * wall_height)

#Prompt user for input
door_count = float(input("Enter the number of Doors: "))

#Door allowance
door_allowance = door_count * door_area

#Prompt user for input
window_count = float(input("Enter the number of Windows: "))

#Window allowance 
window_allowance = window_count * window_area


#Total Area
total_area_sqft = wall_area - (window_allowance + door_allowance)

#Gallons
gallons = math.ceil(total_area_sqft / 300)

#Price
price = float(input("Enter price per gallon of paint: "))

#Cost 
cost = price * gallons 

#Display Output
print("Total sq ft to be painted is", (total_area_sqft))
print("Gallons needed:", gallons)
print(f"Estimated cost: $ {cost:.2f}")














