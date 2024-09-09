# calculator program in Python 
# addition, subtraction, multiplication, and division.

print("A - addition ")
print("B - subtraction ")
print("C - multiplication")
print("D - division")
calculator = input("Enter what you want to do (A|B|C|D) = ").lower()

x = float(input("enter the val 1 = "))
y = float(input("enter the val 2 = "))

if calculator == "a":
    print(f"The addition of {x} and {y} is = {x+y}")
elif calculator == "b":
    print(f"The subtraction of {x} and {y} is = {x-y}")
elif calculator == "c":
    print(f"The multiplication of {x} and {y} is = {x*y}")
elif calculator == "d":
    print(f"The division of {x} and {y} is = {x/y}")
else:
    print("Dont know Man")
    
pr