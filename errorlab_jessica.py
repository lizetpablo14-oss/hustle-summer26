# SNIPPET 1
x = 10
y = 0
divisor = 0
if divisor != 0:
    print("10/divisor")
else:
    print("Error: Cannot divide by zero.")
print("Result:", divisor)
# PREDICT: This code won't run because it's dividing by zero.
# It will print the error message instead of the result.

#SNIPPET 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
# PREDICT: This code will print without the right index since it was at [+1].
# It will print the numbers 1, 2, 3, 4, and 5 correctly.

# SNIPPET 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))
# PREDICT: This code will not run because it's missing a colon at the end. ALso the indentation for the area calculation and return statement.
# It will print the area of a circle with radius 5, which is 78.5.

# SNIPPET 4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))
# PREDICT: It was missing a colon at the end of the if statement. It will print True for 4 and False for 7.
# It will print True for 4 and False for 7.

# SNIPPET 5
for i in range(5):
    print(i)
# PREDICT: Is missing a colon at the end.
# It will print the numbers 0, 1, 2, 3, and 4 correctly.

# SNIPPET 6
def greet(name):
    return "Hello, " + name
print(greet("Alice"))
# PREDICT: It's missing a "+" sign to attach the name to the greeting.
# It will print "Hello, Alice" correctly.

# SNIPPET 7
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)
# PREDICT: It's missing an indentation for the total += number line.
# It will print the sum of the numbers, which is 15.

# SNIPPET 8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
# PREDICT: The n should go down to 0, not 1.
# It will print the factorial of 5, which is 120.

# SNIPPET 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
# PREDICT: It's missing a == before "Bob".
# It will print "Hello, Alice" if the user inputs "Alice", "Hello, Bob" if the user inputs "Bob", and "Hello, stranger!" for any other input.

# SNIPPET 10
def divide_numbers(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    else:
        return x / y

num1 = 10
num2 = 0
print(divide_numbers(num1, num2))
# PREDICT: Zero division error.
# It will print "Error: Cannot divide by zero."

