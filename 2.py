with open('2-input.txt') as file:
    data = file.read().strip()

data = (
    data
    .replace(': ', ' ')
    .replace('-', ' ')
)

# part 1
num_valid = 0

for line in data.split('\n'):
    min, max, char, pwd = line.split(' ')
    min, max = int(min), int(max)
    occurrences = pwd.count(char)
    if occurrences >= min and occurrences <= max:
        num_valid += 1

print num_valid


# part 2
num_valid = 0

for line in data.split('\n'):
    pos_1, pos_2, char, pwd = line.split(' ')
    pos_1, pos_2 = int(pos_1), int(pos_2)
    if (pwd[pos_1 - 1] == char) ^ (pwd[pos_2 - 1] == char):
        num_valid += 1

print num_valid
