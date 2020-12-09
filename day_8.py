with open('day_8_input.txt') as file:
    data = file.read()

instructions = (
    data
    .strip()
    .split('\n')
)

def consruct_graph(instructions):
    redirection_graph = {}

    for line_num, instruction in enumerate(instructions):
        instruction_type, arg = instruction.split(' ')
        arg = int(arg)

        if instruction_type == 'nop':
            redirection_graph[line_num] = (line_num + 1, 0)
        elif instruction_type == 'jmp':
            redirection_graph[line_num] = (line_num + arg, 0)
        elif instruction_type == 'acc':
            redirection_graph[line_num] = (line_num + 1, arg)
    return redirection_graph

def traverse_code_without_repeats(graph):
    line_num = 0
    accumulator = 0
    executed = set()
    while line_num in graph and line_num not in executed:
        executed.add(line_num)
        accumulator += graph[line_num][1]
        line_num = graph[line_num][0]
    return line_num, accumulator


if __name__ == '__main__':
    print('part 1')
    redirection_graph = consruct_graph(instructions)
    end_line, accumulator = traverse_code_without_repeats(redirection_graph)
    print(accumulator)

    print('\n')
    print('part 2')

    from copy import deepcopy


    def is_in_bounds(line_num):
        return line_num >= 0 and line_num < len(instructions)


    for line_num, instruction in enumerate(instructions):
        instruction_type, arg = instruction.split(' ')
        if instruction_type == 'nop':
            modified_graph = deepcopy(redirection_graph)
            modified_graph[line_num] = (line_num + int(arg), 0)
        elif instruction_type == 'jmp':
            modified_graph = deepcopy(redirection_graph)
            modified_graph[line_num] = (line_num + 1, 0)
        else:
            continue

        end_line, accumulator = traverse_code_without_repeats(modified_graph)
        if end_line == 641:
            print('DONE! Flipped line {}'.format(line_num))
            print('Ended on line {}'.format(end_line))
            print('Accumulator value: {}'.format(accumulator))
            break