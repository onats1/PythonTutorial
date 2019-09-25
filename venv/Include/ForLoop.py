

for index in range(1, 11):
    if index == 1:
        print(index)
    elif index == 6:
        continue
    else:
        print("Not the first")


def exponent(base_num, pow_num):
    result = 1
    for counter in range(pow_num):
        result = result * base_num

    return result

def custom_language(text):
    translation = ""
    for letter in text:
        if letter.lower() in "aeiou":
            translation = translation + "y"
        else:
            translation = translation + letter

    return translation

print(custom_language(input("Enter text: ")))