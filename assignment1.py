#BDD
#input
# 1, 2, +
#output
# 3
#behavior
#  Takes in 2 numbers and an operator
#  Returns the result of the operation
#  If the operator is not valid, returns None
#  If the number of arguments is not 3, returns None


def calculate(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  else:
    return None

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")