import re

input_file = open('input.txt', 'r')
input_text = input_file.read()
input_text = input_text.split('\n')

data_table = []

for text in input_text:
    data_table.append([*text])

def find_all_numbers(input_line):
    matches = re.finditer(r'\d+', input_line)
    values = [(int(match.group()), match.start()) for match in matches]
    return values

def find_all_asterisks(input_string):
    matches = re.finditer(r'\*', input_string)
    asterisk_locations = [match.start() for match in matches]
    if asterisk_locations:
        return asterisk_locations
    else:
        return False
    
def get_surrounding_lines(line):
    if line ==0:
        surroundings_lines = input_text[0: 2]
    elif line ==139:
        surroundings_lines = input_text[138::]
    else:
        surroundings_lines = input_text[line-1:line+2]
    
    return surroundings_lines

def get_start_stop(index, value):
    if index == 0:
        start_column, stop_collumn = 0,  len(str(value))+index
    elif len(str(value))+index == 140:
        start_column, stop_collumn = index, 140
    else:
        start_column, stop_collumn = index, len(str(value))+index
    
    return start_column, stop_collumn

def get_start_stop_surroudings(index, value):
    if index == 0:
        start_column, stop_collumn = 0,  len(str(value))+index+1
    elif len(str(value))+index == 140:
        start_column, stop_collumn = index-1, 140
    else:
        start_column, stop_collumn = index-1, len(str(value))+index+1
    
    return start_column, stop_collumn

def get_value_and_surroundings(value, index, line):
    global data_table
    surroundings_lines = get_surrounding_lines(line)
    # print("Value: {} Start: {} End: {} Line: {}".format(value, index, len(str(value))+index , line))

    start_column, stop_collumn = get_start_stop_surroudings(index, value)
    # print(start_column, stop_collumn)

    for line_index, sd_line in enumerate(surroundings_lines):
        surroundings_lines[line_index] = sd_line[int(start_column): int(stop_collumn)]
        # print(sd_line[int(start_column): int(stop_collumn)])

    # print(surroundings_lines)
    return surroundings_lines

asterisk_locations = []
numbers_locations = []

for line in input_text:
    asterisk_locations.append(find_all_asterisks(line))
    numbers_locations.append(find_all_numbers(line))

for row, line in enumerate(numbers_locations):
    print("Row",row, line)
    for number, index in line:
        start, stop = get_start_stop(index, number)
        for column in range(start, stop):
            data_table[row][column] = number
        # print("Start: {} Stop: {} | {}".format(start, stop, data_table[row][start:stop]))

for line_no, locations in enumerate(asterisk_locations):
    if locations != False:
        print("line",line_no)
        for location in locations:
            print(get_value_and_surroundings("*", location, line_no))
    else:
        print("Line {} doesn't include *".format(line_no))
