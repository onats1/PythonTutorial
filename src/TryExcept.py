
try:

    10/0
    print(int(input("Enter a number:")))
except ValueError:
    print("Error")
except ZeroDivisionError as err:
    print(err)