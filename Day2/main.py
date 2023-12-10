
def parse_games():
    input_file = open('input.txt', 'r')
    games = input_file.read()
    games = games.split('\n')

    def parse_game_input(input_string):
        games = input_string.split(';')
        output = []

        for game in games:
            if 'Game' in game:
                game = game.split(':')[1]
            # print(game.strip())
            colors = game.strip().split(',')
            color_counts = []

            for color in colors:
                # print(color.strip().partition(' '))
                count, _, color_name = color.strip().partition(' ')
                color_counts.append([int(count), color_name])

            output.append(color_counts)

        return output

    for index, game in enumerate(games):
        games[index] = parse_game_input(game)

    # for game in games:
    #     print(game)
    
    return games

    min_list = []

    for i in range(len(games)):
        min_list.append([0,0,0])
    
    return min_list

def calcualte_min_game(game, index):
    # print("Game {}".format(index))
    red_min, green_min, blue_min = 0,0,0

    for index, match in enumerate(game):
        # print("Match {}: {}".format(index, match))

        for ball_no, ball_colour in match:
            if ball_colour == 'red' and ball_no > red_min:
                red_min = ball_no
            if ball_colour == 'green' and ball_no > green_min:
                green_min = ball_no
            if ball_colour == 'blue' and ball_no > blue_min:
                blue_min = ball_no
    
    power = red_min * green_min * blue_min

    return [red_min, green_min, blue_min], power


games = parse_games()
total_power = 0

for index, game in enumerate(games):
    min_cubes, power = calcualte_min_game(game, index)
    print("Game {} \t| Min cubes: Red: {} \t| Green: {} \t| Blue: {} \t| Power: {}".format(index+1, min_cubes[0], min_cubes[1], min_cubes[2], power))
    total_power += power

print("Total power:",total_power)
