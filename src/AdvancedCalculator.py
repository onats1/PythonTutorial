
def calculate(operator, num1, num2):
    if operator == "plus" or operator == "+":
        return str(float(num1) + float(num2))
    elif operator == "minus" or operator == "-":
        return str(float(num1) - float(num2))
    elif operator == "multiply" or operator == "*":
        return str(float(num1) * float(num2))
    elif operator == "divide" or operator == "/":
        return str(int(float(num1) / float(num2)))
    else:
        return "Invalid operator"

num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
operator = input("Enter your operator: ")

result = calculate(operator.lower(), num1, num2)
print(round(float(result)))