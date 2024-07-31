import string
import random

def get_random_letter():
    letter = random.choice(string.ascii_letters)
    return letter

def get_random_number():
    number = random.randint(0,9)
    return str(number)

def get_random_special_char():
    special_chars = ["!", "'", "#", "$", "%", "&", "+", "=", "*", "-", "_"]
    special_char = special_chars[random.randint(0, len(special_chars)-1)]
    return special_char

def get_random_char():
    char_type = random.randint(0,2)
    if(char_type == 0):
        return get_random_letter()
    if(char_type == 1):
        return get_random_number()
    if(char_type == 2):
        return get_random_special_char()
    
def generate(length): 
    password = ""

    i = 1
    while i < length+1:
        password += get_random_char()
        i += 1

    return password

print(generate(12))