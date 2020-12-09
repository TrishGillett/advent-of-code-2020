from day_1 import find_pair

with open('day_9_input.txt') as file:
    data = file.read()

numbers = [int(number) for number in data.strip().split('\n')]

def find_contiguous_range_with_total(numbers, total):
    start, end = 0, 0
    while end < len(numbers):
        if sum(numbers[start:end]) == total:
            return numbers[start:end]
        elif sum(numbers[start:end]) < total:
            end += 1
        elif sum(numbers[start:end]) > total:
            start += 1
    return None


if __name__ == '__main__':
    print('part 1')
    for i in range(25, len(numbers)):
        if find_pair(numbers[i-25:i], numbers[i]) is None:
            print("Final answer: {}".format(numbers[i]))
            break


    print('\n')
    print('part 2')
    numbers_sub = find_contiguous_range_with_total(numbers, numbers[i])
    smallest, largest = min(numbers_sub), max(numbers_sub)
    print("Final answer: {}".format(smallest + largest))




