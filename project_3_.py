# unit converter in Python
# kilometers to miles, pounds to kilograms, 
# and Celsius to Fahrenheit:

print("A - kilometers to miles ")
print("B - pounds to kilograms ")
print("C - Celsius to Fahrenheit ")
print("D - miles to kilometers ")
print("E - kilogrms to pounds ")
print("F - fahrenheit to celsius ")
while True:
    converter = input("Enter what you want to do (A|B|C|D|E|F) = ").lower()
    if converter != "a"and"b"and"c"and"d"and"e"and"f":
        break
    
    x = float(input("Enter your val = "))

    if converter == "a" :
        print(f"The kil_to_miles is = {x * 0.621371 } ")
    elif converter == "b" :
        print(f"The miles_to kil is = {x * 1.60934 } ")
    elif converter == "c" :
        print(f"The pou_to_kg is = {x * 0.453592 } ")
    elif converter == "d" :
        print(f"The kg to pou is = {x * 2.20462 } ")
    elif converter == "e" :
        print(f"The cal_to_fahr is = {x + 32 } ")
    elif converter == "f" :
        print(f"The fahr_to_cel is = {x * 5/9 } ")
    else:
        print(" I Dont know ")