# create a program that checks if a number is odd or even

num = int(input('Enter a number: '))

if num % 2 == 0:
    print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')

# create a program that checks if someone can vote or not.
age=int(input('Enter your age: '))
if age >= 18:
    print('You can vote')
else:
    print('Failed. You cannot vote')

# create a program that checks a student grade
grades = int(input('Enter your Marks: '))

if grades <=100 and grades >=80:
    print('You got an A')
elif grades <= 79 and grades >= 60:
    print('You got a B')
elif grades <= 59 and grades >= 40:
    print('You got a C')
elif grades <= 39 and grades >= 0:
    print('You failed terribly!')
else:
    print('Invalid input!')



