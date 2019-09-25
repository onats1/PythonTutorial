
#Basicall you use the words for the conditions such as not instead of ! and or instead of ||
is_male = True
is_present = True

if (is_male or is_present):
    print("You are male and or present")
else:
    print("You are not male and or absent")

if (is_male and is_present):
    print("You are male and or present")
elif(True):
    print("Elif executed.")
else:
    print("You are not male and or absent")

def max_number(num1, num2, num3):
    if(num1 >= num2 and num1 >= num3):
        return num1
    elif(num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3

print(max_number(34, 5, 89))
