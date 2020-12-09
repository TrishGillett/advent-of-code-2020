with open('day_3_input.txt') as file:
    data = file.read()

lines = data.strip().split('\n')

def count_trees(x_slope, y_slope):
    tree_count = 0

    x_pos, y_pos = 0, 0
    while y_pos < len(lines):
        line = lines[y_pos]
        tree_count += int(line[x_pos % len(line)] == '#')
        x_pos += x_slope
        y_pos += y_slope

    return tree_count

print('part 1')
print('answer: {}'.format(count_trees(3, 1)))

print('\n')
print('part 2')
print('slope (1, 1): {}'.format(count_trees(1, 1)))
print('slope (3, 1): {}'.format(count_trees(3, 1)))
print('slope (5, 1): {}'.format(count_trees(5, 1)))
print('slope (7, 1): {}'.format(count_trees(7, 1)))
print('slope (1, 2): {}'.format(count_trees(1, 2)))

print('answer: {}'.format(
    count_trees(1, 1)
    * count_trees(3, 1)
    * count_trees(5, 1)
    * count_trees(7, 1)
    * count_trees(1, 2)
))

