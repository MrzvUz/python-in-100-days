from art import logo
print(logo)

# Add.
def add(n1, n2):
    return n1 + n2


# Substract.
def substract(n1, n2):
    return n1 - n2


# Multiply.
def multiply(n1, n2):
    return n1 * n2


# Devide.
def devide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": devide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operators:
    print(symbol)

operator_symbol = input("Pick an operator from line above: ")
calculation_function = operators[operator_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operator_symbol} {num2} = {answer}")
