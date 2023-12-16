def sort_map(input_string):
    array_to_sort = input_string[1]

    sorted_array = sorted(array_to_sort, key=lambda x: x[0])

    return [input_string[0], sorted_array]
