# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

weight = float(input("Enter the package weight in pounds: "))

if weight <= 2:
    rate = 1.50
elif weight <= 6:
    rate = 3.00
elif weight <= 10:
    rate = 4.00
else:
    rate = 4.75

shipping_cost = weight * rate
print(f"The shipping charge is: ${shipping_cost:.2f}")
# If I did not use 'elif', it does not work.
