my_list = [input().split()]
select = my_list[0][0]
number_1 = my_list[0][1]
number_2 = my_list[0][2]

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

#Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

if select == 'add':
    print(number_1, "+", number_2, "=",
          add(int(number_1), int(number_2)))

elif select == 'subtract':
    print(number_1, "-", number_2, "=",
          subtract(int(number_1), int(number_2)))

elif select == 'multiply':
    print(number_1, "*", number_2, "=",
          multiply(int(number_1), int(number_2)))

elif select == 'divide':
    print(number_1, "/", number_2, "=",
          divide(int(number_1), int(number_2)))
else:
    print("Invalid input")