from numpy import random
import string
import pandas as pd
from general import *

#create file random chars
def create_file_of_random_chars(size):
    with open("random_string.txt", "w") as file:

        for x in range(size):
            y = random.randint(36) 
            y = i_to_chr(y)
            file.write(chr(y))

#create a list of indexes 0-35 representing the chars 
def create_characters_list(string_input):
    """
    the function converts a string to list of ints:
    0-9: values will get converted to 0-9
    A-Z: values will get converted to 10-35
    """
    out_int_list = []
    size = len(string_input)
 
    for char in range(size):
        index = ord(string_input[char]) - 48
        if index >= 10:
            index -= 7
        out_int_list.append(index)

    return out_int_list
