import csv
import numpy  
import pandas as pd
from numpy import random
from create_rand import *

def generate_noise(my_rep_list, path_to_conf):
    file = open(path_to_conf)
    data = pd.read_csv(file)
    size = len(my_rep_list)
    
    for rep_index in range(size):        
        rand_val = random.randint(10000) / 100
        current_probabilities_row = data.iloc[my_rep_list[rep_index]]

        #check if we need to change the character according to probabilities:
        if rand_val <= 100: 
            for replacing_idx in range(1, 37):
                if current_probabilities_row[replacing_idx] < rand_val:       
                    continue
                else:
                    my_rep_list[rep_index] = replacing_idx - 1
                    break
    file.close()



