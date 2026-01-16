# Sample Coding Questions 01 Week 01
# Blossom Babalola

# Questuon 2: Defining an array (list)
my_array = [1, 4, 7, 9]


# Question 3: Order of Operations
a = 1
b = 2
c = 3
d = 4

# Fully-Bracketed Version of: e = a - b ** c // d + a % c
e = (a - ((b ** c) // d)) + (a % c)
print("Question 3 result:", e)

# Question 4: Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# Question 5: User input and type conversion
userAge = input('Enter your age: ')
userAge = int(userAge) + 22
print("Now showing the shop items filtered by age:", userAge)