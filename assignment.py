# Write a function reverse_string (s) that takes a string(s) and returns the reversed string.
def reverse_string(s):
    # s = input('Enter a string: ')
    for i in range(len(s)-1, -1, -1):
        print(s[i], end=' ')

# reverse_string(s=input('Enter a string: '))
reverse_string("Kennedy")


def reverse_string2(s):
    """Reverses a given string.

    Args:
        s: The input string to be reversed.

    Returns:
        The reversed string.
    """

    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage:
string = "hello, world!"
reversed_string = reverse_string2(string)
print('\n', reversed_string)  # Output: !dlrow ,olleh

def reverse_string3(s):
    return s[::-1]
result = reverse_string3('Third Function!')
print(result)



# Palindrome
# Create a function is_palindrome(word) that returns True if a given word is a palindrome (reads the same backward) and False otherwise.
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("hello"))
print(is_palindrome("madam"))
print(is_palindrome("racecar"))


# Write a function Fibonacci(n) that generates a lists containing the first n numbers in the Fibonacci sequence.
def fibonacci(n):
  """Generates a list containing the first n Fibonacci numbers.

  Args:
    n: The number of Fibonacci numbers to generate.

  Returns:
    A list of the first n Fibonacci numbers.
  """

  if n <= 0:
    return []

  fib_list = [0, 1]
  while len(fib_list) < n:
    next_fib = fib_list[-1] + fib_list[-2]
    fib_list.append(next_fib)

  return fib_list[:n]

# Example usage:
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci(20))


def fibonnaci2(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    for i in range(2, n):
        # fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return  fib_sequence

print(fibonnaci2(5))
print(fibonnaci2(10))
print(fibonnaci2(20))