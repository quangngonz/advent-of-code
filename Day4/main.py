import re

def process_input_file(file_name):
    input_file = open(file_name, 'r')
    input_text = input_file.read()
    input_text = input_text.split('\n')
    input_file.close()

    def split_numbers(input_string):
        numbers = re.findall(r'\d+', input_string)  
        numbers = [int(num) for num in numbers] 
        return numbers

    def print_winning_cards(index, winning_numbers_card):
        print("Card: {} \tWinning:".format(index + 1), end=" ")
        print(*winning_numbers_card, sep=", ")

    cards = []
    cards_winning_numbers = []

    for card in input_text:
        card_name, _ , card_content = card.partition(": ")
        winning_numbers, _ , numbers = card_content.partition(" | ")

        winning_numbers = split_numbers(winning_numbers)
        numbers = split_numbers(numbers)

        cards.append([winning_numbers, numbers])

    for index, card in enumerate(cards):
        winning_numbers_card = []
        winning_numbers, numbers = card[0], card[1]

        for number in numbers:
            if number in winning_numbers:
                winning_numbers_card.append(number)

        cards_winning_numbers.append(winning_numbers_card)
        # If you want to print, call the function here:
        # print_winning_cards(index, winning_numbers_card)

    return cards_winning_numbers

winning_copies = [1] * 198

file_name = 'input.txt'
results = process_input_file(file_name)

for card_no, result in enumerate(results):
    copies_card = winning_copies[card_no]

    if len(result) != 0:
        for _ in range(copies_card):
            for other_card in range(card_no+1, card_no+len(result)+1):
                winning_copies[other_card] += 1

print("Total number of scratchcards:", sum(winning_copies))
