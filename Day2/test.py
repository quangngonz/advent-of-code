def possible_games(cubes_count, games):
    possible = []
    for game in games:
        valid = True
        for subset in game:
            counts = subset.split(', ')
            total_red = sum(int(count.split()[0]) for count in counts if 'red' in count)
            total_green = sum(int(count.split()[0]) for count in counts if 'green' in count)
            total_blue = sum(int(count.split()[0]) for count in counts if 'blue' in count)
            
            if total_red > cubes_count['red'] or total_green > cubes_count['green'] or total_blue > cubes_count['blue']:
                valid = False
                break
        
        if valid:
            possible.append(int(game[0][5:].split(':')[0]))
    
    return possible

def main():
    # Configuration of cubes
    cube_counts = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    
    # Reading input from the file
    with open('input.txt', 'r') as file:
        games = [line.strip().split('; ') for line in file.readlines()]
    
    possible = possible_games(cube_counts, games)
    total_possible = sum(possible)
    print(f"The games that would have been possible: {possible}")
    print(f"The sum of the IDs of those games: {total_possible}")

if __name__ == "__main__":
    main()
