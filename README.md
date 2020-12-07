before running the program:
1. create a folder on your current path to store the configuration files: ./config_files
2. run gaussian_noise.py/drift_noise.py/random_noise.py to create automatically noise csv files (gauss.csv / drift.csv / random.csv)

run in terminal:
python3 server.py \n\t*a file with random string (100,000 chars A-Z, 0-9) will be created on your current path (random_string.txt)

in another terminal: 
python3 client.py \n\t*you will be asked to choose path to store the data (original & noise) and the figures (1/20 of the figures are saved)
