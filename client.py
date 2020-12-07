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
    acumulated_char_list = [0 in range(36)]
    fig = plt.figure()

    #recieving/sending:
    counter = 0 #will be used for unique filenames
    while message.lower().strip() != 'quit':
        counter += 1
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        
        if data == 'eof':  #'eof' will be sent from server when work is done
            message = 'quit'
            continue

        #creating noisy input from recieved data, and saving to file
        characters_list = create_characters_list(data)
        generate_noise(characters_list, "config_files/"+ noise_type+ ".csv")
        save_char_list_to_file(characters_list, data, counter, path)
        
        acumulated_char_list += characters_list
        draw_dynamically(acumulated_char_list, plt, fig, counter, path)
        
    client_socket.close()  # close the connection

if __name__ == '__main__':  
    client_program()
