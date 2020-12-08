import socket
import pandas
import os
import matplotlib.pyplot as plt
from create_rand import *
from generate_noise import *
from general import *

NUM_OF_CHARS = 36

def client_program():
    """
    the function gets chunks of 100 chars from server. then it:
    1. inputs noise to the string
    2. saving the original & noised string inside a folder created by this 
        function
    3. saving once in 20 chunks the histogram of the current noised string
    4. drawing accumulative histogram of the recived chunks 
    5. responsible of closing the connction when all data has been read
    """ 

    path = input("please choose name of folder to store data & figures: ")
    os.mkdir(path)
    
    noise_type = input("gauss / drift / random: ")
    
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "void"
    acumulated_char_list = [0 in range(NUM_OF_CHARS)] #for drawing accumulative histogram
    fig = plt.figure()

    #recieving/sending:
    counter = 0 #will be used for unique filenames
    while message.lower().strip() != 'quit':
        counter += 1
        client_socket.send(message.encode())  # send message
        recieved_string = client_socket.recv(1024).decode()  # receive response
        
        if recieved_string == 'eof':  #'eof' will be sent from server when work is done
            message = 'quit'
            continue

        noised_string = generate_noise(recieved_string, "config_files/"+ noise_type + ".csv")
        save_string_to_file(recieved_string, noised_string, counter, path)
        noised_int_list = create_characters_list(noised_string)
        acumulated_char_list += noised_int_list
        draw_dynamically(acumulated_char_list, fig, counter, path)
        
    client_socket.close()  # close the connection

if __name__ == '__main__':  
    client_program()
