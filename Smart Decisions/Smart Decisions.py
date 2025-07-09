import time

name = input("What is your name? ")
GPA = float(input("What is your current GPA? "))
Hours = float(input("How many hours did you sleep last night? "))
InputExam = input("Do you have an exam tomorrow? (Y/N) ")
Exam = ""


if (GPA >=3.5):
    print("You're doing great academically!")
elif (GPA <=3.49 and GPA >=2.5):
    print("You're doing okay, but there's room to grow.")
else:
    print("Let's talk strategies to raise your grades.")

if (InputExam == "Y" and Hours <6):
    print("You need more rest! Try a power nap and light review.")
    Exam = "Yes"
elif (InputExam == "Y" and Hours >= 6):
    print("You're on track- review your notes and get confident!")
    Exam = "Yes"
else:
    print("Use today to catch up or get ahead- balance is key.")
    

time.sleep(1)
print("")
print("")

print(f"Good Luck {name}")
print(f"Your GPA is {GPA}")
print(f"You got {Hours} of sleep.")
print(f"Exam Tomorrow: {Exam}")
print(f"Advice: Rest up for tomorrow, but dont forget to study before doing so. It's been proven that studying during the hours 8pm-10pm have proven to help with memory.")
