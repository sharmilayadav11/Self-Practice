first_number = input("Enter first number: ")
operator = input("Enter any Operator (+,-,*,/,%): ")
second_number = input("Enter second number: ")

first_number = int(first_number)
second_number = int(second_number)

if operator == "+":
    print(first_number + second_number)

elif operator == "-":
    print(first_number - second_number)

elif operator == "*":
    print(first_number * second_number)

elif operator == "/":
    print(first_number / second_number)

elif operator == "%":
    print(first_number % second_number)

else:
    print("invalid Operators")
