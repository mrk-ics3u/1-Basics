# Lesson 1 - Basics

The example code for this lesson is in `basics.py`. Open it alongside these
notes and run it as we go.

## Printing strings

When printing strings (text) there are three quote levels you can use. Single
quotes (apostrophes) are the most common. Double quotes are mainly used when
the string itself contains an apostrophe (for example "What's going on?"). The
triple quote (three apostrophes) is mainly used when the string contains both a
double quote and an apostrophe.

```python
print('Hello world!')
print("Hello world!")
print('''Hello World!''')

print('''Mr K says "Who's there?"''')
```

## Variables and printing

Variables temporarily store information and can be manipulated in many ways.
A variable should be named descriptively, so it is easy to tell what the value
it holds represents.

Variables can be of different types:

- integers (whole number values)
- floats (decimal values)
- characters (single character)
- strings (multiple characters / text)
- Boolean values (True or False)
- and more

```python
# variables
integer_one = 19.8
integer_two = 22
greeting = 'Hello'

# printing
print(integer_one)
print(integer_one - integer_two)
print(greeting)
```

Normally we will not print variables on their own. We want a message to go
along with the value, and there are a few ways to do that.

```python
integer_one = 15
integer_two = 22

# comma separated
print('Our first integer value is', integer_one, 'units.')

# f-strings
print(f'Our second integer value is {integer_two} units.')

# string concatenation
# note that the integer variable (integer_one) is converted to a string
print('Our first integer value is ' + str(integer_one) + ' units.')
```

## snake_case

A variable name should be descriptive and should also follow the snake_case
(or pot_hole_case) convention, where all words are separated by underscores.
This makes your code more readable.

```python
# not readable
mystudentsname = 'Amir'
# readable
my_students_name = 'Christina'
```

## Mathematical operations

You can use the standard operators `+`, `-`, `*` and `/`, plus a few you may
not have used before:

- `//` integer division, which drops the decimal part
- `%` modulo, the remainder after a division
- `**` a power

```python
first_number = 17
second_number = 5

print(first_number + second_number)    # 22
print(first_number - second_number)    # 12
print(first_number * second_number)    # 85
print(first_number / second_number)    # 3.4, division always gives a float
print(first_number // second_number)   # 3
print(first_number % second_number)    # 2
print(first_number ** second_number)   # 1419857
```

Note that `/` always produces a float, even when the division comes out even.
`10 / 5` is `2.0`, not `2`.

## Converting between types

You can convert between data types with functions such as `int()`, `float()`
and `str()`.

```python
number_as_text = '42'

print(int(number_as_text) + 8)     # 50
print(float(number_as_text))       # 42.0
print(str(99) + ' bottles')        # 99 bottles
```

## Constants

Sometimes we want a value that is fixed and can be referred to by name, such as
PI. Writing `PI` is shorter and clearer than typing the digits every time.

The difference between a constant and a variable is that a constant should
never be modified. In Python we write constants in all uppercase. Python will
not stop you from changing the value, so the uppercase letters are a reminder
to you, the programmer, not to.

```python
# constants - uppercase letters remind us not to modify
PI = 3.14159
TEACHER_NAME = "Mr K"
COURSE_SUBJECT = "Computer Science"
```

## Receiving input from the user

Sometimes you want someone to enter information so your program can process it
and print something back. We use the `input()` function, which takes one
argument: the question to show the user, as a string.

```python
name = input('Enter your name: ')
print(name)
```

The program prompts with `Enter your name: `, waits for the user to type
something and press Enter, then prints what was entered.

`input()` always hands back a **string**, even when the user types digits. If
you want to do math with it, convert it first.

```python
age = input('Enter your age: ')
print(f'Next year you will be {int(age) + 1}.')
```

## Lab

That is it for the lesson. Move on to Lab 1, in `README.md`.
