from parse_input import parse_data
from sort_map import sort_map

def create_list(max_no):
    blank_list = []
    for i in range(max_no + 1):
        blank_list.append(i)
    
    return blank_list

data = parse_data()
default_list = create_list(10)

names = ["seeds", "seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

seeds = data[0][1][0]
maps = data[1:]

map_name_index = 0
map_numbers_index = 1

for index, mapping in enumerate(maps):
    sorted_map = sort_map(mapping)
    maps[index] = sorted_map

for test_index in range(len(maps)):
    print(maps[test_index][0])

    for index, numbers in enumerate(maps[test_index][1]):
        no_range = numbers[2]
        try:
            end_source = (numbers[0] + no_range) == maps[test_index][1][index+1][0]
        except:
            end_source = "End value"

        if end_source == False:
            print(numbers, "e_source: {} {} {}".format(numbers[0] + no_range, maps[test_index][1][index+1][0], end_source))
