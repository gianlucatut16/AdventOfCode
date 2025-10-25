def string_get_instructions(line):
    line_split = line.split()
    quantity = int(line_split[1])
    init_stack = int(line_split[3]) - 1
    fin_stack = int(line_split[5]) - 1
    return quantity, init_stack, fin_stack

stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

moves = open('instructions_ex.txt', 'r')

i = 1

# print('########### First Half ###########')
# for move in moves:
#     quantity, init_stack, fin_stack = string_get_instructions(move)
    
#     for _ in range(quantity):
#         tmp = stacks[init_stack].pop()
#         stacks[fin_stack].append(tmp)

#     # print(f'################## Move {i} ##################')
#     # print(f'{stacks}\n')
#     # i+=1

# print('Final stacks:')
# for j in range(len(stacks)):
#     print(f"Stack_{j+1}: ", stacks[j])

print('########### Second Half ###########')
for move in moves:

    quantity, init_stack, fin_stack = string_get_instructions(move)
    stacks[fin_stack] = stacks[fin_stack] + stacks[init_stack][len(stacks[init_stack]) - quantity : len(stacks[init_stack])]
    stacks[init_stack] = stacks[init_stack][0 : len(stacks[init_stack]) - quantity]
    print(stacks)
