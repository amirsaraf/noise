import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from general import *

def create_drift_noise(filename):
    """creates right-drift config file"""
    file =  open(filename, 'w', newline='')
    writer = csv.writer(file)
    noise_level = int(input("choose noise level (1-100):"))

    #create header values:
    header = [chr(i_to_chr(i)) for i in range(36)]
    writer.writerow(np.append(np.array("CHAR"), header))

    #create 36 additional rows:
    for i in range(36):
        zeros = [0 for i in range(36)]
        temp_arr = np.append(np.array(chr(i_to_chr(i))), zeros)
        temp_arr[(i+2) % 37] = noise_level
        
        if i == 35:
            temp_arr[0] = 'Z'
        writer.writerow(temp_arr)
    file.close()

if __name__ == '__main__':
    create_drift_noise("config_files/drift.csv")
