import re

input_file = open('input.txt', 'r')
input_text = input_file.read()
input_text = input_text.split('\n')

def split_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)  
    numbers = [int(num) for num in numbers] 
    return numbers

def calculate_points(winning_nos):
    points = 0
    if len(winning_nos) == 0:
        return 0
    elif len(winning_nos) == 1:
        return 1
    else:
        power = len(winning_nos) -1
        return 2**power

cards = []

for card in input_text:
    card_name, _ , card_content = card.partition(": ")
    winning_numbers, _, numbers = card_content.partition(" | ")

    winning_numbers = split_numbers(winning_numbers)
    numbers = split_numbers(numbers)

    cards.append([winning_numbers, numbers])

total_points = 0

for index, card in enumerate(cards):
    points = 0
    winning_numbers_card = []
    winning_numbers, numbers = card[0], card[1]
    
    # print(winning_numbers, numbers)

    for number in numbers:
        if number in winning_numbers:
            winning_numbers_card.append(number)
    
    points = calculate_points(winning_numbers_card)

    print("Card: {} \tPoints: {} \tWinning: {}".format(index+1, points, winning_numbers_card))
    total_points += points

print("Total", total_points)
