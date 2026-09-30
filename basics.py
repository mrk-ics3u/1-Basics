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
integer_one = 19.8
integer_two = 22
greeting = 'Hello'

# printing
print(integer_one)
print(integer_one - integer_two)
print(greeting)


# --- Printing variables with a message ---------------------------------------
integer_one = 15
integer_two = 22

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

# storing into a variable



# --- Converting between types ------------------------------------------------
number_as_text = '42'

print(int(number_as_text) + 8)     # text converted to an integer, then added
print(float(number_as_text))       # text converted to a float
print(str(99) + ' bottles')        # number converted to text, then joined


# --- Constants ---------------------------------------------------------------
# constants - uppercase letters remind us not to modify
PI = 3.14159
TEACHER_NAME = "Mr K"
COURSE_SUBJECT = "Computer Science"

print(f'{TEACHER_NAME} teaches {COURSE_SUBJECT}, and pi is about {PI}.')


# --- Input -------------------------------------------------------------------
name = input('Enter your name: ')
print(name)

# input() always hands back a string, so convert it before doing math
age = input('Enter your age: ')
print(f'Next year you will be {int(age) + 1}.')
