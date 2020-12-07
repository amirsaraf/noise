import numpy as np
import matplotlib.pyplot as plt
import csv
from general import *
 
def create_normal_dist(filename):
    data = np.random.randn(1000)
    values, base = np.histogram(data, bins=36) 
    noise_level = input("choose noise level (1-100):")
    cumulative = np.cumsum(values)/1000
    cumulative = cumulative * int(noise_level)
       
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        header = []
        header.append('CHAR')

        for i in range(36):
            i = i_to_chr(i)
            header.append(chr(i))
        writer.writerow(header)

        for i in range(36):
            i = i_to_chr(i)
            cumu_new = np.array(chr(i))
            new_arr = np.append(cumu_new, cumulative)
            writer.writerow(new_arr)
        file.close()

if __name__ == '__main__':
    create_normal_dist("config_files/gauss.csv")