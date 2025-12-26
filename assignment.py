# palindrome
# display first n fibonacci numbers
# two sum problem

# Basic Class Creation
# Create a Book class with attributes: title, author, and price. Include a method to display book information.

class Book:
    title = None
    author = None
    price = 0.0

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

demo = Book()
demo.title = "1984"
demo.author = "George Orwell"
demo.price = 9.99
demo.display_info()

# Constructor Practice

# Design a Student class that takes name, student_id, and grade in the constructor. Add a method to update the grade.

class student:
    def __init__(self,name,student_id,grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade
    def display_student(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")
stud1 = student("Alice", "S123", "A")
stud1.display_student()
stud1.update_grade("A+")
stud1.display_student()