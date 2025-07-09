import time

age = float(input("How old are you "))

if age>= 18:
    print("Your an adult")
else:
    print("Your a minor")

time.sleep(2)

grade = float(input("What is your test score: "))

if grade >= 90:
    print("A!")
elif grade >= 80 and grade<=89:
    print("B!")
elif grade >= 70 and grade<=79:
    print("C!")
elif grade >= 60 and grade<=69:
    print("D!")
else:
    print("F!")

time.sleep(2)

option = input("You’re standing at a fork in the road. Do you go left or right? (use lowercase letters) ")

if option == "left":
    print("You Found Pirate BOOTAYH BOIIIII")

elif option == "right":
    print("You died!...loser.")
else:
    print("You stand still like the bum you are, unsure of what to do next")

time.sleep(2)

Q1 = input("You got a ticket? (use lowercase letters) ")
Q2 = float(input("How old are you?"))

if Q1 == "yes" and Q2 >=18:
    print("you may enter!")
else:
    print("leave")