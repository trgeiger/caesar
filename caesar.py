from helpers import rotate_character, alphabet_position


def encrypt(text, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    capalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_text = ""
    for char in text:
        if char in alpha:
            index = alphabet_position(char)
            index = (index + rot) % 26
            new_text = new_text + alpha[index]
        elif char in capalpha:
            index = alphabet_position(char)
            index = (index + rot) % 26
            new_text = new_text + capalpha[index]
        else:
            new_text = new_text + char
    return new_text


"""
#Execution of program with validation preceding encrypt()

validargs = user_input_is_valid(argv)
if validargs == False:
    print("Please enter a valid integer argument after caesar.py")
    exit()
print(encrypt(input("Enter your secret message: "), int(argv[1])))
"""
