import numpy as np
import matplotlib.pyplot as plt
import csv
from general import *

NUM_OF_CHARS = 36

def create_random_noise(filename):
    """creates random probability matrix in a csv file"""
    noise_level = int(input("choose noise level (1-100):"))
    
    file =  open(filename, 'w', newline='')
    writer = csv.writer(file)
    
    #create header values:  
    header = [chr(i_to_chr(i)) for i in range(NUM_OF_CHARS)]
    writer.writerow(np.append(np.array("CHAR"), header))

    for i in range(NUM_OF_CHARS):
        data = np.random.rand(noise_level)
        values, base = np.histogram(data, bins=NUM_OF_CHARS)
        cumulative = np.cumsum(values)

        writer.writerow(np.append(np.array(chr(i_to_chr(i))), cumulative))

    file.close()

if __name__ == '__main__':
    create_random_noise("config_files/random.csv")