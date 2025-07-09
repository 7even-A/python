name = input("Whats Your name? ")
weekly_income = float(input("What is your weekly income? "))
rent = float(input("What is your rent? "))
groceries = float(input("What is your cost of groceries? "))
transportation = float(input("What is your cost of transportation? "))
is_student = input("Are you a student? (Y/N) ")

total_expenses = rent + groceries + transportation
money_left = weekly_income - total_expenses

# print(total_expenses)
# print(money_left)



print(f"Hello,  {name}!")
print(f"Weekly Income: {weekly_income}")
print(f"Total Expenses: {total_expenses}")
print(f"Money Left: {money_left}")

if (is_student == "Y" or is_student == "y" or is_student == "yes" or is_student == "true" or is_student == "True"):
    print("Student Discount Applied: True")
else:
    print("Student Discount Applied: False")
