from parse_input import parse_data

def find_max(input_list):
    max_source, max_destination = 0, 0

    numbers = input_list[1]

    for item in numbers:
        source = item[0]
        destination = item[1]
        map_range = item[2]

        end_source = source + map_range
        end_destination = source + map_range

        if end_source > max_source:
            max_source = end_source
        
        if end_destination > max_destination:
            max_destination = end_destination

        # print("Source: {} \tDestination: {} \tRange: {}".format(source, destination, map_range))

    return max_source, max_destination

# Test cases
# data = parse_data()

# seeds = data[0][1][0]
# seed_to_soil = data[1]

# print(find_max(seed_to_soil))
