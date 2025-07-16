def welcome_message():
    print("Welcome to the Function Factory")


welcome_message()


def greet_user(name):
    print(f"Hello, {name}! Hope you're having a great day.")


name = input("What is your name? ")
greet_user(name)


def add_numbers(num1, num2):
    print(f"The sum is: {num1 + num2}")

numb1 = float(input("Enter a number: "))
numb2 = float(input("Enter another number: "))

add_numbers(numb1, numb2)

def get_age(yr):
    age = 2025 - yr
    print(f"You are {age} years old")

year = int(input("What year were you born? "))

get_age(year)

def check_if_odd(num):
    if (num % 2 == 0 ):
        print("not odd")
    else:
        print("odd")

ONumb = float(input("Enter a number: "))
check_if_odd(ONumb)


def motivation():
    print("You got this! Be confident, and look the part!")

motivation()