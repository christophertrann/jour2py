#ex1

def native_csv_read(csv_file):
    with open(csv_file, 'r') as file:
        
        lines = file.readlines()
        
        lines = lines[1:]
        
        result = []
        for index, line in enumerate(lines):

            line = line.strip()

            columns = line.split(';')

            result.append((index,) + tuple(columns))
    
    return result

csv_data = native_csv_read('orders_semicolon.csv')
print(csv_data)

#ex2
