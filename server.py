import pandas as pd
import socket
import time
from create_rand import create_file_of_random_chars

def server_program():
    """
    server side: 
    1. creates a random 100K chars string
    2. sending the string by chunks of 100 chars
    3. when all data has been read, it sends 'eof' to the client
    """
    create_file_of_random_chars(100_000)
    
    host = socket.gethostname()# get the hostname
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(1) # 1 client
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    in_file = open("random_string.txt", "rb") # opening for [r]eading as [b]inary

    while True:
        # receive data stream. up to 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break  # if data is not received break
        
        chunk = in_file.read(100) 
        
        if (chunk == b''):
            chunk = b'eof'
        conn.send(chunk) 

    conn.close()  
    in_file.close()

if __name__ == '__main__':
    server_program()
