# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
#Options
print("Menu:")                                                                                      
print("1. Hot Dog - $3.50")                                                                         
print("2. Chili Dog - $4.50")                                                                       
                                                                                                    
choice = int(input("Enter 1 for Hot Dog or 2 for Chili Dog: "))                                     
 # here you chose between the 2                                                                                                   
if choice == 1:                                                                                     
    base_price = 3.50                                                                               
else choice == 2:                                                                                   
    base_price = 4.50                                                                               
            # addions if any, it should work                                                                                        
cheese = input("Would you like cheese? ($0.50) (yes/no): ").strip().lower() == "yes"                
peppers = input("Would you like peppers? ($0.75) (yes/no): ").strip().lower() == "yes"              
onions = input("Would you like grilled onions? ($1.00) (yes/no): ").strip().lower() == "yes"        
                                                                                                    
toppings_cost = (0.50 if cheese else 0) + (0.75 if peppers else 0) + (1.00 if onions else 0)        
subtotal = base_price + toppings_cost                                                               
tax = subtotal * 0.07                                                                               
total = subtotal + tax                                                                              
                                                                                                    
print(f"Hot Dog Cost: ${base_price:.2f}")                                                           
print(f"Toppings Cost: ${toppings_cost:.2f}")                                                       
print(f"Tax (7%): ${tax:.2f}")                                                                      
print(f"Total Cost: ${total:.2f}")    
#Final prices and everything
