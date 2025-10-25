with open('real_input.txt', 'r') as file:
    data = file.read()

grid = [item for item in data.split('\n')]

coords_dict = {}
for ind_row in range(len(grid)):
    for ind_col in range(len(grid[0])):
        char = grid[ind_row][ind_col]
        if char != '.':
            if char in coords_dict.keys():
                coords_dict[char].append((ind_row, ind_col))
            else:
                coords_dict[char] = [(ind_row, ind_col)]


def check_antinode_in_grid(grid, antinode):
    width, height = len(grid[0]), len(grid)

    if (0 <= antinode[0] < width) and (0 <= antinode[1] < height):
        return True
    else:
        return False


def find_antinode(ant_1, ant_2):
    x_dist = ant_1[0] - ant_2[0]
    y_dist = ant_1[1] - ant_2[1]

    antinode_1 = ant_1[0] + x_dist, ant_1[1] + y_dist
    antinode_2 = ant_2[0] - x_dist, ant_2[1] - y_dist


    return antinode_1, antinode_2


def find_antinode_2(ant_1, ant_2):

    antinodes = [ant_1, ant_2]
    x_dist = ant_1[0] - ant_2[0]
    y_dist = ant_1[1] - ant_2[1]

    antinode = ant_1[0] + x_dist, ant_1[1] + y_dist
    while check_antinode_in_grid(grid, antinode):
        antinodes.append(antinode)
        antinode = antinode[0] + x_dist, antinode[1] + y_dist

    antinode = ant_2[0] - x_dist, ant_2[1] - y_dist
    while check_antinode_in_grid(grid, antinode):
        antinodes.append(antinode)
        antinode = antinode[0] - x_dist, antinode[1] - y_dist

    return antinodes


score = 0
antinodes = []
for item in coords_dict:
    cord_lst = coords_dict[item]
    for i in range(len(cord_lst) - 1):
        for j in range(i + 1, len(cord_lst)):

            # an_1, an_2 = find_antinode(cord_lst[i], cord_lst[j])
            # if (check_antinode_in_grid(grid, an_1)) and (an_1 not in antinodes):
            #     antinodes.append(an_1)
            #     score += 1
            
            # if (check_antinode_in_grid(grid, an_2)) and (an_2 not in antinodes):
            #     antinodes.append(an_2)
            #     score += 1
            ants_temp = find_antinode_2(cord_lst[i], cord_lst[j])
            for an in ants_temp:
                if an not in antinodes:
                    antinodes.append(an)
                    score += 1

print(score)