def parse_input(calibration_string):
    number_words = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    no_words = ['zero', 'one', 'two', "three", "four", "five", "six", "seven", "eight", "nine"]
    word_index = []
    output_string = calibration_string

    def find_all_indexes(string, target):
        indexes = []
        start = 0
        while True:
            index = string.find(target, start)
            if index == -1:
                break
            indexes.append(index)
            start = index + 1
        return indexes

    for word in no_words:
        locations = find_all_indexes(calibration_string, word)
        if locations != []:
            word_index.append((word, locations))

    for word, indices in word_index:
        for index in indices:
            output_string = output_string[:index] + number_words[word] + output_string[index+1:]

    print(word_index)

    return output_string

file_content = open('day1_2.txt', 'r')
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
    new_value = parse_input(value)
    print(value, new_value)
    first_number = return_first_number(new_value)
    last_number = return_last_number(new_value)
    print(first_number + last_number)
    calibration_value = int(first_number + last_number)

    total += calibration_value

print(total)   
