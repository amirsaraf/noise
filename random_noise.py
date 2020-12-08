import numpy as np
import matplotlib.pyplot as plt
import csv
from general import *

def create_random_noise(filename):
    noise_level = int(input("choose noise level (1-100):"))
    
    file =  open(filename, 'w', newline='')
    writer = csv.writer(file)
    
    #create header values:  
    header = [chr(i_to_chr(i)) for i in range(36)]
    writer.writerow(np.append(np.array("CHAR"), header))

    for i in range(36):
        data = np.random.rand(noise_level)
        values, base = np.histogram(data, bins=36)
        cumulative = np.cumsum(values)

        writer.writerow(np.append(np.array(chr(i_to_chr(i))), cumulative))

    file.close()

if __name__ == '__main__':
    create_random_noise("config_files/random.csv")