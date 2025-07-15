class Student():
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
    
    def __str__(self):
        return(f"Student: {self.name}, ID:  {self.student_id}, Grades: {self.grades}, averge grade: {(sum(self.grades)/len(self.grades))}")

    def add_grade(self, grade):
            self.grades.append(grade)
            print(self.grades)

    def get_average(self):
         total = sum(self.grades)
         
         divisor = len(self.grades)

         avg = total/divisor

         return avg

    def has_passed(self, avg):
         

         if (avg >= 60):
              return True
         else:
              return False
    

    def get_letter_grade(self, avg):
         if (avg > 90):
              return "A"
         elif (avg > 80 and avg <89):
            return "B"
         elif (avg > 70 and avg <79):
            return "C"
         elif (avg > 60 and avg <69):
            return "D"
         else:
            return "F"
         
    def reset_grades(self):
        self.grades = []


X = Student("Joe", "9", [95,67,86])
print(X)
X.add_grade(96)
print(X.get_average())
print(X.has_passed(X.get_average()))
print(X.get_letter_grade(X.get_average()))
X.reset_grades()
print(X.grades)


#len, #sum