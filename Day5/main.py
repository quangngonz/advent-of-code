
def parse_data():
    input_file = open("input.txt", "r")
    input_data = input_file.read()
    input_data = input_data.split("\n\n")

    data = []

    for chunk in input_data:
        name, _, numbers = chunk.partition(":\n")
        numbers = [int(num) for num in numbers.replace('\n', ' ').split()]
        data.append([name, numbers])
    
    return data

data = parse_data()
