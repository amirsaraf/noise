def i_to_chr(i):
    if i > 9:
        i += 7
    i += 48
    return i

#translating the recieved signal back to string
def save_char_list_to_file(original_string, noised_string,  counter, path):
    with open("./" + path + "/" + str(counter)+'.txt', 'w') as file:
            file.write("original string:\n")
            file.write(original_string)
                       
            file.write("\nnoised string:\n")
            file.write(noised_string)

#drawing histogram function
def draw_dynamically(acumulated_char_list, plt, fig, counter, path):
    plt.hist(acumulated_char_list, bins = 36)
    plt.xlim(0, 35)
    plt.ylim(0, sum(acumulated_char_list)/200)
    plt.draw()  
    plt.pause(0.05)
    
    if (not counter % 20):
        fig.savefig("./" + path + "/" + str(counter) + '.png')
    
    fig.clear()
    
    