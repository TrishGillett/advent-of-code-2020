from collections import defaultdict

with open('day_10_input.txt') as file:
    data = file.read()

numbers = [0] + sorted([int(number) for number in data.strip().split('\n')])


def count_ways(numbers, start, num_ways_starting_from):
    total_num_ways = 0
    for i in range(start+1, len(numbers)):
        if numbers[i] > numbers[start] + 3:
            break

        if numbers[i] not in num_ways_starting_from:
            num_ways_starting_from = count_ways(numbers, i, num_ways_starting_from)
        total_num_ways += num_ways_starting_from[numbers[i]]

    num_ways_starting_from[numbers[start]] = total_num_ways
    return num_ways_starting_from


if __name__ == '__main__':
    print('part 1')
    diff_freqs = defaultdict(int)
    for i in range(1, len(numbers)):
        diff_freqs[numbers[i] - numbers[i-1]] += 1
    diff_freqs[3] += 1
    print(diff_freqs[1] * diff_freqs[3])


    print('\n')
    print('part 2')
    num_ways_starting_from = defaultdict(int)
    num_ways_starting_from[numbers[-1]] = 1
    print(count_ways(numbers, 0, num_ways_starting_from))






