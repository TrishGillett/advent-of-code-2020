with open('6-input.txt') as file:
    data = file.read()

groups = (
    data
    .strip()
    .split('\n\n')
)

print('part 1')
running_sum = 0
for group in groups:
    group = group.replace('\n', '')
    count_distinct = len(set(list(group)))
    running_sum += count_distinct

print(running_sum)

print('\n')
print('part 2')
running_sum = 0
for group in groups:
    people = group.split('\n')
    yes_set = set(list(people[0]))
    for person in people[1:]:
        yes_set = yes_set.intersection(set(list(person)))
    count_distinct = len(yes_set)
    running_sum += count_distinct

print(running_sum)
