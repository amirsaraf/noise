import numpy as np
import matplotlib.pyplot as plt
import csv
from general import *

def create_random_noise(filename):
    noise_level = input("choose noise level (1-100):")
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        header = []
        header.append('CHAR')

        for i in range(36): #create first line in csv -> all relevant chars
            i = i_to_chr(i)
            header.append(chr(i))
        writer.writerow(header)

        for i in range(36):
            i = i_to_chr(i)
            data = np.random.rand(int(noise_level))
            values, base = np.histogram(data, bins=36)
            cumulative = np.cumsum(values)
            csv_keys = np.array(chr(i))
            new_arr = np.append(csv_keys, cumulative)
            writer.writerow(new_arr)
        file.close()

if __name__ == '__main__':
    create_random_noise("config_files/random.csv")