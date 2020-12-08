import csv
import numpy  
import pandas as pd
from numpy import random
from create_rand import *

def generate_noise(my_string, path_to_conf):
    """the function genertes noise to input string, using a given path to 
    config file"""
    file = open(path_to_conf)
    chars_list = pd.read_csv(file, index_col = "CHAR", nrows = 0).columns
    file.close()

    file = open(path_to_conf)
    data = pd.read_csv(file, index_col = "CHAR")
    file.close()

    out_string = ''
    
    for index in range(len(my_string)):     #index is for my_string    
        current_probabilities_row = data.loc[my_string[index]]
        #make choice to replace char or not
        rand_val = random.randint(10000) / 100
        if rand_val <= 100: 
            for replacing_idx in range(36): #replacing_idx is for the prob. 
                
                if rand_val <= current_probabilities_row[replacing_idx]:   
                    out_string += chars_list[replacing_idx]
                    break
        if replacing_idx == 35:
            out_string += my_string[index]

    return out_string            
    