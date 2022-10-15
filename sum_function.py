def sum(number1, number2 = 20):
    return number1 + number2

# you should have new line after function for PEP8 Standard
number1 = 15
number2 = 10

print(f"The Sum of {number1}  +  {number2} is :  {sum(number2 = number1, number1 = number2)} ")