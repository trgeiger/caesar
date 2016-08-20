#helper functions for crypto problem set

def alphabet_position(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    return(alpha.index(letter))

def rotate_character(char, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    capalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_char = ""
    if char in capalpha:
        index = alphabet_position(char)
        index = (index + rot) % 26
        new_char = capalpha[index]
    elif char in alpha:
        index = alphabet_position(char)
        index = (index + rot) % 26
        new_char = alpha[index]
    else:
        new_char = char
    return new_char
