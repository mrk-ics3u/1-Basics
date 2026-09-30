#-----------------------------------------------------------------------------
# Name:        Basics (basics.py)
# Purpose:     Demonstrating strings, variables, printing, math operators,
#              type conversion, constants and input()
#
# Author:      Mr. Kowalczewski
# Created:     23-Sept-2026
# Updated:     23-Sept-2026
#-----------------------------------------------------------------------------

# --- Printing strings --------------------------------------------------------
print('Hello world!')
print("Hello world!")
print('''Hello World!''')

print('''Mr K says "Who's there?"''')


# --- Variables ---------------------------------------------------------------
# variables
float_one = 19.8 #float
integer_two = 22 #int
greeting = 'Hello' #string
is_late = True #boolean

# printing
print(float_one)
print(float_one - integer_two)
print(greeting)


# --- Printing variables with a message ---------------------------------------
integer_one = 15
integer_two = 28 #variables CAN change throughout the program

# comma separated
print('Our first integer value is', integer_one, 'units.')

# f-strings
print(f'Our second integer value is {integer_two} units.')

# string concatenation
# note that the integer variables (integer_one) is converted to a string - more on that later.
print('Our first integer value is ' + str(integer_one) + ' units.')


# --- snake_case --------------------------------------------------------------
# not readable
mystudentsname = 'Amir'
# readable
my_students_name = 'Christina'


# --- Mathematical operations -------------------------------------------------
first_number = 17
second_number = 5

print(first_number + second_number)    # addition
print(first_number - second_number)    # subtraction
print(first_number * second_number)    # multiplication
print(first_number / second_number)    # division, always gives a float
print(first_number // second_number)   # integer division, drops the decimal
print(first_number % second_number)    # modulo, the remainder
print(first_number ** second_number)   # power

# storing into a variable (so you can use the result later!)
math_result = 10 / 2 + 5
print(f"math_result is: {math_result}")


# --- Converting between types ------------------------------------------------
number_as_text = '42'

# we can convert between types with int(), float() and str()
# this is needed sometimes if you are trying to perform math operations
print(int(number_as_text) + 8)
print(type(number_as_text)) # number_as_text is still a string!
number_as_text = int(number_as_text) # variable is converted, and then stored back into the variable
print(type(number_as_text))
print(float(number_as_text))       
print(str(99) + ' bottles')        


# --- Constants ---------------------------------------------------------------
# constants - uppercase letters remind us not to modify
PI = 3.14159
TEACHER_NAME = "Mr K"
COURSE_SUBJECT = "Computer Science"

print(f'{TEACHER_NAME} teaches {COURSE_SUBJECT}, and pi is about {PI}.')


# --- Input -------------------------------------------------------------------

# when using the input() function, the user's response is returned
# you must store it in a variable in order to make use of it later!
name = input('Enter your name: ')
print(f"Hello {name}!")

# what's wrong with this? input() always gives strings!
age = int(input('Enter your age: '))
#age = int(age)
age += 1 # short form of age = age + 1
print(f'Next year you will be {age}.')
