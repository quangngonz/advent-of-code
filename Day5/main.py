from find_biggest_value import find_max
from parse_input import parse_data

def create_list(max_no):
    blank_list = []
    for i in range(max_no + 1):
        blank_list.append(i)
    
    return blank_list

data = parse_data()
default_list = create_list(10)

names = ["seeds", "seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

seeds = data[0][1][0]

for index, mapping in enumerate(data[1:]):
    print("{}\t max_source {} \tmax_destination {}".format(names[index], find_max(mapping)[0], find_max(mapping)[1]))
