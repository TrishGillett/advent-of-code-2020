with open('day_5_input.txt') as file:
    data = file.read()

binary_encoded_seats = (
    data
    .strip()
    .replace('F', '0')
    .replace('B', '1')
    .replace('L', '0')
    .replace('R', '1')
    .split('\n')
)

def get_seat_id(binary_encoded_seat):
    return int(binary_encoded_seat, 2)

print('part 1')
max_id = max([get_seat_id(seat) for seat in binary_encoded_seats])
print(max_id)

print('\n')
print('part 2')

possible_seat_ids = set(range(max_id+1))
claimed_seat_ids = set([get_seat_id(seat) for seat in binary_encoded_seats])
unclaimed_seat_ids = possible_seat_ids - claimed_seat_ids

my_seat = [
    seat_id
    for seat_id in unclaimed_seat_ids
    if not unclaimed_seat_ids.intersection(set([seat_id + 1, seat_id - 1]))
]
print(my_seat)