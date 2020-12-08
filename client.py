import socket
import pandas
import os
import matplotlib.pyplot as plt
from create_rand import *
from generate_noise import *
from general import *

def client_program():
    path = input("please choose name of folder to store data & figures: ")
    os.mkdir(path)
    
    noise_type = input("gauss / drift / random: ")
    
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "void"
    acumulated_char_list = [0 in range(36)] #for drawing accumulative histogram
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
        save_char_list_to_file(recieved_string, noised_string, counter, path)
        noised_int_list = create_characters_list(noised_string)
        acumulated_char_list += noised_int_list
        draw_dynamically(acumulated_char_list, plt, fig, counter, path)
        
    client_socket.close()  # close the connection

if __name__ == '__main__':  
    client_program()
