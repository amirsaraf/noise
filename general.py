import matplotlib.pyplot as plt
from collections import Counter

NUM_OF_CHARS = 36

def i_to_chr(i):
    """
    the function converts an int to a desired ascii value:
    0-9   ---> 48-57
    10-35 ---> 65-90
    """
    if i > 9:
        i += 7
    i += 48
    return i

#translating the recieved signal back to string
def save_string_to_file(original_string, noised_string, counter, path):
    """saving 2 strings to a file in a given path"""
    with open("./" + path + "/" + str(counter)+'.txt', 'w') as file:
            file.write("original string:\n")
            file.write(original_string)
                       
            file.write("\nnoised string:\n")
            file.write(noised_string)

#drawing histogram function
def draw_dynamically(acumulated_char_list, fig, counter, path):
    """dynamic drawing function. 
    the function also saves plot to files (once in 20 iterations)"""
    
    letter_counts = Counter(acumulated_char_list)
    plt.bar(letter_counts.keys(), letter_counts.values())
    plt.draw()
    
    if (not counter % 20):
        fig.savefig("./" + path + "/" + str(counter) + '.png')
    
    plt.pause(0.1)
    fig.clear()
    
    