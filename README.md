# Lab 1 - Name, Age and Numbers

Open `main.py` and complete the following:

1. Update the header with your information (Name, Purpose, Author, Created, Updated).
2. Prompt the user with `What is your name? ` and store the answer in a variable.
3. Prompt the user with `How old are you? ` and store the answer in a variable.
4. Print `Hello ____, you are currently ____ years old.` with their name and age in the blanks.
5. Add 10 to their age.
6. Print `In 10 years, you will be ____ years old.` with the new age in the blank.
7. Prompt the user with `Enter a number: ` and store the answer in a variable. Assume it is an integer.
8. Prompt the user with `Enter another number: ` and store the answer in a variable. Assume it is an integer.
9. Print the seven results below, one per line, using the first number and the second number.

```
Sum: ____
Difference: ____
Product: ____
Quotient: ____
Integer Division: _____
Modulo: ______
Power: ______
```

Every prompt above ends with a space after the question mark or colon. Copy the
prompt text exactly as it is written here, including that space.

Print only what is asked for, and nothing extra.

## Running your program

Open `main.py` and press the Run button in the top right corner of VS Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B** to run the tests. You will see one line per test:

```
[PASS] 1. Header is filled in
[FAIL] 2. Works for Alice, 15, 6 and 3
```

When a test fails it shows what was expected and what your program printed. Fix your code and press Ctrl+Shift+B again. Keep going until all tests pass.

## Reminders

- Fill in every field of the header before you write any code.
- Use descriptive variable names in snake_case.
- Write comments as you go. One comment can cover a few related steps, for example steps 2 to 4.
- Tests check your output exactly. Capitals and punctuation matter, so `sum: 9` is not the same as `Sum: 9`.
- `input()` gives you a string. Convert it with `int()` before doing math.
