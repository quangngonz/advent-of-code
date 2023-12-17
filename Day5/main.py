from parse_input import parse_data
from sort_map import sort_map

def create_list(max_no):
    blank_list = []
    for i in range(max_no + 1):
        blank_list.append(i)
    
    return blank_list

data = parse_data()
default_list = create_list(10)

map_names = ["seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]

seeds = data[0][1][0]
maps = data[1:]

map_name_index = 0
map_numbers_index = 1

for index, mapping in enumerate(maps):
    sorted_map = sort_map(mapping)
    maps[index] = sorted_map

def find_dest(source, mapping):
    destination = source

    mapping_name = mapping[0].split(" ")[0]
    source_name , _, destination_name = mapping_name.split("-")
    map_numbers = mapping[1]

    for source_start, dest_start, map_range in map_numbers:
        source_end = source_start + map_range - 1
        
        if source_start <= source <= source_end:
            difference = source - source_start
            destination = dest_start + difference

            print()
            print(mapping_name)
            print(source_start, dest_start, map_range)

    return source_name, destination_name, destination

all_answers = []

for seed in seeds:
    seed_values = [seed]

    for index in range(len(map_names)):
        source_name, dest_name, dest = find_dest(seed_values[-1], maps[index])

        print(source_name, seed_values[-1], dest_name, dest)

        seed_values.append(dest)
    
    all_answers.append(seed_values)
    
    print("_______________________________________________")

all_answers = sorted(all_answers, key=lambda x: x[-1])

print(all_answers[0])
