MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

input_file = open('input.txt', 'r')
games = input_file.read()
games = games.split('\n')

total_invalid_ids = []
total_valid_ids = []

def parse_game_input(input_string):
    games = input_string.split(';')
    output = []

    for game in games:
        if 'Game' in game:
            game = game.split(':')[1]
        colors = game.strip().split(',')
        color_counts = []

        for color in colors:
            count, _, color_name = color.strip().partition(' ')
            color_counts.append([int(count), color_name])

        output.append(color_counts)

    return output

def check_cube(cube):
    if cube[1] == 'blue' and cube[0] > MAX_BLUE:
        return False
    elif cube[1] == 'red' and cube[0] > MAX_RED:
        return False
    elif cube[1] == 'green' and cube[0] > MAX_GREEN:
        return False
    else:
        return True

for index, game in enumerate(games):
    games[index] = parse_game_input(game)

for index, game in enumerate(games):
    game_id = index+1
    game_validity = True
    # print("Game:", game_id, end = "\t")

    for match in game:
        for cube in match:
            if check_cube(cube) == False:
                # print("Game impossible", cube)
                game_validity = False
                break
        
        if game_validity == False:
            break
    
    if game_validity == False:
        total_invalid_ids.append(game_id)
    else:
        # print("Game possible")
        total_valid_ids.append(game_id)

print("Possible games: {} \nSum IDs: {}".format(total_valid_ids, sum(total_valid_ids)))
print("Impossible games: {} \nSum IDs: {}".format(total_invalid_ids, sum(total_invalid_ids)))
