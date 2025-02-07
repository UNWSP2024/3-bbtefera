# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:

# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 year old, it should display "adult".

def categorize_age(age):
    
age = float(input("Enter the person's age: "))

    if age <= 1:
        category = "infant"
    elif age < 13:
        category = "child"
    elif age < 20:
        category = "teenager"
    else:
        category = "adult"

print(f"The person is classified as: {category}")
# It should work. I ran it through PyCharm to make sure
