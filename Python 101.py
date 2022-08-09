#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python and My First Python Codes

# ## Why Python? 

# <p> You’re not a programmer but some of your friends are. You don’t know what programmers do until one day you saw a friend of yours did the coding with Python and you realized how cool it is to learn programming. Based on your friend’s suggestion, you want to start with Python. </p>

# <p>So, the first thing you do is “Googling” what is Python and how you can get a job with it. Thanks to Google, you only need to type “What is Python?” and the Search Engine will give you about 1,400,000,000 results. No, I’m serious! The Google will give you about 1,400,000,000 results! Now you feel overwhelmed and that it’s impossible for you to learn Python. But trust me, the best defense is knowledge and confidence in the skills that will keep you alive, whether it's for a few hours, days, or long term. </p>

# <p>Ok, let’s get started </p>

# <p><b>1.	What is Python? </b><br>
# 
# According to Kuhlman, Dave. "A Python Book: Beginning Python, Advanced Python, and Python Exercises", “Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.”<br>
# 
# Ok now it’s getting more complicated, but you don’t have to memorize it or try to understand word by word. You only need to know that Python is a general-purpose programming language that can be used to build website or create a variety of different programs. Moreover, since it’s easy to learn, it’s adopted by many non-programmers such as scientists or business analysts. If they can do it, so can you!</p>
# 
# <p><b>2.	How to get started?</b></p>
# 
# <p><ul>
#     <li>You can download Python for free on https://www.python.org/downloads/ website </li>
#     <li> Make sure you download the latest pip version because you will need it to import Python packages/modules later</li></ul>    
# 

# ![picture.png](attachment:picture.png)

# <p><b>3. What is IDE?</b></p>

# <p>IDE is Integrated Development Environment and is used to code and run Pythom programs on your own computer</p>
# <p>Top 10 popular IDE that Pythom programmers use:</p>
# <ol>
#     <li>IDLE</li>
#     <li>PyCharm</li>
#     <li>Visual Srudio Code</li>
#     <li>Jupyter Notebook</li>
#     <li>Antom</li>
#     <li>Sublime Text</li>
#     <li>Spyder</li>
#     <li>PyDev</li>
#     <li>Vim</li>
#     <li>Thony</li>
# </ol>
# <p> For my first Python Codes, I will use Jupyter NoteBooks. You can use pip to install Jupyter Notebook in cmd. And to use Jupyter Notebook, you can open cmd and type "jupyter notebook".</p>

# ![jp.png](attachment:jp.png)

# <p>You can start creating your first Python project by hitting the "Next" button on the top right corner and choose "Python 3 (ipykernel)</p>

# ![jp1.png](attachment:jp1.png)

# ## My First Python Codes

# ### Comment Your Python Code

# <p> Comments are great way to leave notes to yourself and to other people in case you will later need to figure out what those codes do. Also, comments in Python can be used to make the code more readable. THus, it's always considered a great practice to keep your comment clear and consise. </p>
# <p>There are two ways to write comments in Python</p>
# <ul>
#     <li> Using # to tell Python to ignore the text on the current line </li>
#     <p>Example:<br/>
#     <p># This is a comment</p><br/>
#     <li> For multi-line comments, you can use the triple quotes</li>
#     <p>Example:<br/>
#     <p>""" These are <br/>
#         multi-lines <br/>
#         comments <br/>
#         """</p>
# </ul>

# ### Variables

# <p> Python variable is a container for storing data values </p>
#     <p>For example: <br>
#     country = "U.S.A"</p>
# <p> The following exercise is to create lines of code to ask a new student his/her name and say hello to that person.   
#     

# In[1]:


# Ask a new student for his/her name
student_name = input("What's your name? ")

# Say hello to the new student
print("Hello,", student_name)


# <p>There is another way to print out the name of the student</p>

# In[2]:


# Ask a new student for his/her name

student_name = input("What's your name? ")

# Say hello to the new student
print("Hello, ")
print(student_name)


# In[4]:


# If you don't want 'Hello, Andy' to be shown in two different lines but still keep the codes in 2 lines, you can do this:

# Ask a new student for his/her name
student_name = input("What's your name? ")

# Say hello to the new student

print("Hello,", end =" ")
print(student_name)


# In[8]:


# Also, there is another way to print the name of the student by using Formatted String Literals

studdent_name = input("What's your name? ")
print(f"Hello, {student_name}")


# In[11]:


# Let's try to add more variables

# Ask a new student for his/her name
student_name = input("What's your name? ")

# Ask his/her ID number
id = input("What's your ID number? ")

print(f"Hello, {student_name} , ID number {id}. Welcome to Finance 101 class!")

