# python program to create a simple calculator
# 3 steps to create the our simple calculator
#  1. function for operators
#  2. use input
#  3. print result

# function to add 2 numbers
def add(num1,num2):
    return num1 + num2

# function substract 2 numbers
def sub(num1,num2):
    return num1 - num2

# function multiply 2 numbers
def multiply(num1,num2):
    return num1 * num2

# function divide 2 numbers
def divide(num1,num2):
    return num1 / num2

# function average 2 numbers
def avg(num1,num2):
    return (num1 + num2) / 2

# user input
print("please select a operator:\n" \
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n")

select = int(input("Select a Operator from 1 to 5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter Second number: "))

# Print the result
if select == 1:
    print(number1, "+", number2, "= ", \
          add(number1,number2))

elif select == 2:
    print(number1, "-", number2, "= ", \
          sub(number1,number2))

elif select == 3:
    print(number1, "*", number2, "= ", \
          multiply(number1, number2))

elif select == 4:
    print(number1, "/", number2, "= ", \
          divide(number1 , number2))

elif select == 5:
    print("(",number1, "+", number2, ")", "/", "2" "= ", \
          avg(number1 , number2))

else:
    print("Invaild operator! Please select again")