#first calculator program in python

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("result of operations on", a, "and", b, "are as follows:")
print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)

if b !=0:
    print("division :", a / b)
    print("floor division :", a // b)
    print("modulus :", a % b)
    print("percentage :", (a / b) * 100)
else:
    print("division : not possible")
    print("floor division : not possible")
    print("modulus : not possible")
    print("percentage : not possible")

print("Thank you for using the calculator!")
print("made by: @harshpatel")
