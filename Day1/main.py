
file_content = open('day1.txt', 'r')
calibration_list = file_content.read().split('\n')
file_content.close()

total = 0

def return_first_number(input_string):
    for char in input_string:
        if char.isdigit():
            return char
        
def return_last_number(input_string):
    new_string_list = input_string[::-1]
    for char in new_string_list:
        if char.isdigit():
            return char

for value in calibration_list:
    first_number = return_first_number(value)
    last_number = return_last_number(value)
    calibration_value = int(first_number + last_number)

    total += calibration_value

print(total)    
