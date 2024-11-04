 # 1. Check in a student named John Doe into the hostels. He is 21 years old and He is a
 # new student.
 # Declare three variables to store: name, age and if he is a new or old student. Output
 # this status message:
 # He has been admitted to the hostels.
 # At Time: 12:52:50PM
name = 'John Doe'
age = 21
status = 'new'
if status == 'new':
    print('He has been admitted to the hostels. \nAt Time: 12:52:50PM')
else:
    print('He is an old student')

# 2. Create a program that asks the user to enter their name and their age. Print out a
#  message addressed to them that tells them the year that they will turn 100 years old,
 # except use f-strings instead of the + operator to print the resulting output message.
name = input('What is your name?: ')
age = int(input('How old are you?: '))

from datetime import date
current_year = date.today().year
hundredth_birthday_year = current_year + (100-age)

print(f'Hi {name}, you will turn 100 years old in the year {hundredth_birthday_year}.')

#  3. write as a simple program that prompts the user to enter two numbers. Then,
#  configure the program to perform various arithmetic operations on the two numbers,
#  including addition, subtraction, multiplication, division, and exponentiation and print
#  the results.
print('Enter two numbers:')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

multiply = num1 * num2
div = num1 / num2
add = num1 + num2
sub = num1 - num2
exponent = num1 ** num2

print(f'The sum is {add}')
print(f'The difference is {sub}')
print(f'The product is {multiply}')
print(f'The Division is {div}')
print(f'The exponent is {exponent}')

# 4. write a program that allows the user to enter their weights in kilograms or pounds and
#  then converts the user weight input to the other unit.
weight = int(input('What is your weight in kilograms?: '))
pounds = weight * 2.20462
print(f'The weight in pounds is {pounds:.2f}')

 # 5. Write a Python program that prompts the user to enter a numerical grade between 0
 # and 100, and then prints the corresponding congratulatory message based on the
 # following grading scale:
 # 90 and above: good job ( >=95 excellent )
 # 80 to 89: well done
 # 70 to 79: keep it up
 # 60 to 69: average
 # Below 60: needs improvement
grade = int(input('Enter your grade between 0 and 100: '))
if grade >= 95:
    print('Excellent')
elif grade >= 90:
    print('Good job')
elif grade >= 80:
    print('Well done')
elif grade >= 70:
    print('Keep it up')
elif grade >= 60:
    print('Average')
else:
    print('Needs improvement')

# 6. Create a program that asks the user to enter their name and their age. Print out a
#  message addressed to them that tells them the year that they will turn 100 years old.
age = int(input('Enter your age: '))
name = input('Enter your name: ')

current_year = date.today().year
hundredth_birthday_year = current_year + (100-age)

print(f'Hi {name}, you will turn 100 years old in the year {hundredth_birthday_year}.')

# 7. Add onto the previous program by asking the user for another number and printing
#  out that many copies of the previous message. Print out many copies of the previous
#  message on separate lines.
loop = int(input('How many times do you want to print the previous message: '))
for i in range(loop):
    print(f'Hi {name}, you will turn 100 years old in the year {hundredth_birthday_year}.')

# 8. Choose a secret number. prompt the user to guess your secret number. allow the user
#  to guess a maximum of three times and give him a feedback of whether the guess is
#  right or wrong.
secret_number = 5
guesses_left = 3

while guesses_left > 0:
    guess = int(input('Guess a number between 0 and 10: '))
    guesses_left -= 1
    if guess == secret_number:
        print('Congratulations! You guessed the correct number!')
        break
    else:
        print('Sorry, you guessed the wrong number! Try again!')
if guesses_left == 0:
    print(f'You have run out of guesses. The correct number is {secret_number}')

# 9. Write a Python program that takes a sentence as input from the user and counts the
#  number of words in the sentence.
#  Your program should remove any leading or trailing spaces from the sentence and
#  consider a word to be any sequence of characters separated by spaces.
sentence = input('Enter a sentence: ')
sentence = sentence.strip()
words = sentence.split()
word_count = len(words)
print('Number of words:', word_count)

# 10. Write a Python program that takes a positive integer n as input and prints a pattern
#  consisting of n rows and n columns. The pattern should be a square shape with
#  alternating characters 'X' and 'O'.
n = int(input('Enter a positive integer: '))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('X', end=' ')
        else:
            print('O', end=' ')
    print()