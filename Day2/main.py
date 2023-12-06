import re

games_list_temp = []
game_list_final = []

input_file = open('input.txt', 'r')
games = input_file.read()
games = games.split('\n')

for game in games:
    games_list_temp.append(game.split(":")[1])

for index, game in enumerate(games_list_temp):
    games_list_temp[index] = game.split(";")

    m_matches = []

    for matches in games_list_temp[index]:
        m_matches.append(matches.split(","))

        for index, match in enumerate(m_matches):
            for index, cube in enumerate(match):
                m_matches[index] = re.findall(r'\d+', cube)


    game_list_final.append(m_matches)

print(game_list_final[0])
