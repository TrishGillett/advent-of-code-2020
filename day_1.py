with open('day_1_input.txt') as file:
    data = file.read().strip()

numbers = [int(num_str.strip()) for num_str in data.split('\n')]

def find_pair(num_list, sum):
    num_list = sorted(num_list)
    for i, small_num in enumerate(num_list):
        if small_num > 0.5*sum:
            # Viable 'small number' candidates can't be larger than this
            break

        for larger_num in reversed(num_list):
            if small_num + larger_num == sum:
                # print 'numbers: {}, {}'.format(small_num, larger_num)
                # print 'product: {}'.format(small_num * larger_num)
                return small_num, larger_num
            elif small_num + larger_num < sum:
                # Since we're checking 'larger number' candidates in descending order,
                # we won't find successful candidates past this point
                break
    return None

def find_trio(num_list, sum):
    num_list = sorted(num_list)
    for i, small_num in enumerate(num_list):
        if small_num > sum/3.0:
            # Viable 'small number' candidates can't be larger than this
            break

        for med_num in num_list[i+1:]:
            for larger_num in reversed(num_list):
                if larger_num < med_num:
                    break
                elif small_num + med_num + larger_num < sum:
                    # Since we're checking 'larger number' candidates in descending order,
                    # we won't find successful candidates past this point
                    break
                elif small_num + med_num + larger_num == sum:
                    print 'numbers: {}, {}, {}'.format(small_num, med_num, larger_num)
                    print 'product: {}'.format(small_num * med_num * larger_num)

if __name__ == '__main__':
    # part 1: find a pair of numbers in the list that sum to 2020
    # approach: Sort numbers, focus on fixing the small number and then looking for an appropriate large number

    print('part 1')
    find_pair(numbers, 2020)
    print('')

    # part 2: find a trio of numbers in the list that sum to 2020
    # approach: Sort numbers, focus on fixing the small number and a medium number and then looking for an appropriate large number

    print('part 2')
    find_trio(numbers, 2020)
