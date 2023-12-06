input_file = open('input.txt', 'r')
games = input_file.read()
games = games.split('\n')

def parse_game_input(input_string):
    games = input_string.split(';')
    output = []

    for game in games:
        if 'Game' in game:
            game = game.split(':')[1]
        print(game.strip())
        colors = game.strip().split(',')
        color_counts = []

        for color in colors:
            print(color.strip().partition(' '))
            count, _, color_name = color.strip().partition(' ')
            color_counts.append([int(count), color_name])

        output.append(color_counts)

    return output

for index, game in enumerate(games):
    games[index] = parse_game_input(game)

for game in games:
    print(game)