# while loop

num =2

while num <= 15:
    print(f'loop: {num}')
    num += 2

# create a while loop that initial 100 to zero with a difference of 5 each
# decremental loop

num2 = 100
while num2 >= 0:
    print(f"loop: {num2}")
    num2 -= 5

# for loop
name = ['Ashlynn', 'Chris', 'Raf', 'April', 'Rex']

for i in name:
    print(i)

num3 = [12, 2, 32, 24, 25, 6, 7, 23, 9, 8, 4, 23]
total = 0

for n in num3:
    total += n
print(f' The total of the element is: {total}')

myschool = 'emobilis'
for m in myschool:
    print(m)

# even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print(even)