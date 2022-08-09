
# Ask a new student for his/her name
student_name = input("What's your name? ")

# Say hello to the new student
print("Hello,", student_name)


# There is another way to print out the name of the student
# Ask a new student for his/her name
student_name = input("What's your name? ")

# Say hello to the new student
print("Hello, ")
print(student_name)


# If you don't want 'Hello, Andy' to be shown in two different lines but still keep the codes in 2 lines, you can do this:

# Ask a new student for his/her name
student_name = input("What's your name? ")

# Say hello to the new student
print("Hello,", end =" ")
print(student_name)


# Also, there is another way to print the name of the student by using Formatted String Literals
student_name = input("What's your name? ")
print(f"Hello, {student_name}")


# Let's try to add more variables

# Ask a new student for his/her name
student_name = input("What's your name? ")
# Ask his/her ID number
id = input("What's your ID number? ")
print(f"Hello, {student_name} , ID number {id}. Welcome to Finance 101 class!")

