#ex1
def read_one_line(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
    return first_line
file_name = 'exemple.txt'
line = read_one_line(file_name)
if line is not None:
    print(f"La première ligne est : '{line}'")
else:
    print("Aucune ligne lue.")

#ex2
def write_to_file(filename, text):
    file = open(filename, 'w')  
    file.write(text)            
    file.close() 
write_to_file('fichier.txt', 'texte.')

#ex3
def copy_characters(input_file, output_file, nb):

    with open(input_file, 'r') as src_file:
       
        content = src_file.read(nb)
    
    with open(output_file, 'a') as dst_file:
        
        dst_file.write('\n')
       
        dst_file.write(content)
copy_characters('source.txt', 'destination.txt', 10)

#ex4
def read_all_lines(filename):
 
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    every_other_line = lines[::2]
    
    return (lines, every_other_line)

all_lines, alternate_lines = read_all_lines('ex4.txt')
print("Toutes les lignes :", all_lines)
print("Une ligne sur deux :", alternate_lines)

read_all_lines('ex4.txt')
#ex5

def write_to_file(filename, text):
    
    with open(filename, 'w') as file:
        file.write(text)

write_to_file('fichier.txt', 'texte.')


def copy_characters(input_file, output_file, nb):
    
    with open(input_file, 'r') as src_file, open(output_file, 'a') as dst_file:
        
        content = src_file.read(nb)
        
        if dst_file.tell() > 0:
            dst_file.write('\n')
        
        dst_file.write(content)

copy_characters('source.txt', 'destination.txt', 10)






            
