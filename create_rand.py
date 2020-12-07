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
    rep_lut = []
    size = len(string_input)
 
    for char in range(size):
        index = ord(string_input[char]) - 48
        if index >= 10:
            index -= 7
        rep_lut.append(index)

    return rep_lut



# #create random list of A-Z / 0-9
# def create_rand_list(size):
#     string_input = ""

#     for x in range(size):
#         y = random.randint(36) 
#         string_input += chr(y)

#     return string_input

# def create_rand_list_pd(size):
#     string_input = []

#     for x in range(size):
#         y = random.randint(36) 
#         t = i_to_chr(y)
#         string_input.append(chr(y))
#         ser = pd.Series(string_input, dtype ="string")
        
#     return ser