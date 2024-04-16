import re

input_file = open('input_2.txt', 'r')
input_text = input_file.read()
input_text = input_text.split('\n')

data_table = []

for text in input_text:
    data_table.append([*text])

def get_values_index(input_line):
    matches = re.finditer(r'\d+', input_line)
    values = [(int(match.group()), match.start()) for match in matches]
    return values

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

    start_column, stop_collumn = get_start_stop(index, value)
    # print(start_column, stop_collumn)

    for line_index, sd_line in enumerate(surroundings_lines):
        surroundings_lines[line_index] = sd_line[int(start_column): int(stop_collumn)]
        # print(sd_line[int(start_column): int(stop_collumn)])

    # print(surroundings_lines)
    return surroundings_lines

def check_valid(value, index, line):
    validity = False
    surrounding_lines = get_value_and_surroundings(value, index, line)

    check_symbol = re.compile("[!@#$%&*()_+=|<>?{}\\[\\]/~-]")
    for line_content in surrounding_lines:
        if check_symbol.search(line_content):
            validity = True

    print("Value: {} Start: {} End: {} Line: {}".format(value, index, len(str(value))+index , line))
    
    for line_content in surrounding_lines:
        print(line_content)

    print("Validity:", validity)
    print("__________________________________________________________")
    return validity

value_index_by_lines = []
value_and_valid = []

for line in input_text:
    value_index_by_lines.append(get_values_index(line))

for line, line_numbers in enumerate(value_index_by_lines):
    print("Line {}: {}".format(line, line_numbers))
    for value, index in line_numbers:
        value_validity = check_valid(value, index, line)
        value_and_valid.append((value, value_validity))

sum_parts = 0

for value, valid in value_and_valid:
    if valid:
        sum_parts += value

print("Sum of parts:", sum_parts)
