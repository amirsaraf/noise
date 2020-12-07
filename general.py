def i_to_chr(i):
    if i > 9:
        i += 7
    i += 48
    return i

#translating the recieved signal back to string
def save_char_list_to_file(characters_list, data,  counter, path):
    temp_str = '' 
    for i in characters_list: 
        j = i_to_chr(i)
        temp_str += chr(j)

    with open("./" + path + "/" + str(counter)+'.txt', 'w') as file:
            file.write(temp_str)
            file.write("\n\n\noriginal string:\n")
            file.write("----------------\n")                
            file.write(data)

#drawing histogram function
def draw_dynamically(acumulated_char_list, plt, fig, counter, path):
    plt.hist(acumulated_char_list, bins = 36)
    plt.xlim(0, 35)
    plt.ylim(0, sum(acumulated_char_list)/180)
    plt.draw()  
    plt.pause(0.05)
    
    if (not counter % 20):
        fig.savefig("./" + path + "/" + str(counter) + '.png')
    
    fig.clear()
    
    