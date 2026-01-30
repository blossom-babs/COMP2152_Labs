'''
Docstring for Week03.Q4

Question 4: Class Attendance (Sets - Uniqueness and Operations)
Concepts: Set creation, add(), remove(), union (|), intersection (&), difference (-)

Create a program to track class attendance:

'''

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
both_classes = monday_class & wednesday_class
print(f"Attended both classes: {both_classes}")
either_class = monday_class | wednesday_class
print(f"Attended either class: {either_class}")
only_monday = monday_class - wednesday_class
print(f"Only Monday: {only_monday}")
only_one_class = monday_class ^ wednesday_class
print(f"Only one class (not both): {only_one_class}")
is_subset = monday_class <= either_class
print(f"Is Monday subset of all students? {is_subset}")