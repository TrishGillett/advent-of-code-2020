with open('day_7_input.txt') as file:
    data = file.read()

rules = (
    data
    .strip()
    .replace(' bags', '')
    .replace(' bag', '')
    .replace(' no ', ' 0 ')
    .replace('.', '')
    .split('\n')
)

print('part 1')
def get_outer_bags(bag, checked):
    bag_types = set()
    for rule in rules:
        outer_bag, inner_bags = rule.split(' contain ')
        if bag in inner_bags:
            bag_types.add(outer_bag)
    checked.add(bag)

    for bag in bag_types:
        if bag not in checked:
            rec_bag, rec_checked = get_outer_bags(bag, checked)
            bag_types = bag_types.union(rec_bag)
            checked = checked.union(rec_checked)
    return bag_types, checked

bag_types, _ = get_outer_bags('shiny gold', set())
print(len(bag_types))

print('\n')
print('part 2')
mapping = {}
for rule in rules:
    outer_bag, inner_bags = rule.split(' contain ')
    inner_bags = [(int(bag_count.split(' ')[0]), ' '.join(bag_count.split(' ')[1:])) for bag_count in inner_bags.split(', ')]
    mapping[outer_bag] = inner_bags

def count_inner(bag):
    count = 1
    for bag_num, bag_type in mapping[bag]:
        if bag_num != 0:
            count += bag_num * count_inner(bag_type)
    return count

print(count_inner('shiny gold') - 1)

