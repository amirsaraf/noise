import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from general import *

def create_drift_noise(filename):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        header = []
        header.append('CHAR')

        for i in range(36):
            i = i_to_chr(i)
            header.append(chr(i))
        writer.writerow(header)

        noise_level = int(input("choose noise level (1-100):"))
        for i in range(36):
            j = i_to_chr(i)
            
            cumu2 = np.array(chr(j))
            zeros = [0 for i in range(36)]
            new_arr = np.append(cumu2, zeros)
            new_arr[(i+2) % 37] = noise_level
           
            if i == 35:
                new_arr[0] = 'Z'
                #new_arr[1] = noise_level
            writer.writerow(new_arr)
        
if __name__ == '__main__':
    create_drift_noise("config_files/drift.csv")
