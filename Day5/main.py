
def parse_data():
    input_file = open("input.txt", "r")
    input_data = input_file.read()
    input_data = input_data.split("\n\n")
    input_file.close()

    data = []

    for chunk in input_data:
        name, _, numbers = chunk.partition(":\n")
        numbers = numbers.split("\n")

        for index, number in enumerate(numbers):
            numbers[index] = number.split(" ")

        data.append([name, numbers])
    
    return data

data = parse_data()
