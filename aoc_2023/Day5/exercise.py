def string_get_instructions(line):
    line_split = line.split()
    quantity = int(line_split[1])
    init_stack = int(line_split[3]) - 1
    fin_stack = int(line_split[5]) - 1
    return quantity, init_stack, fin_stack

file = open('instructions_ex.txt', 'r')
stack_line = file.readline()
num_row = 0
while stack_line.split()[0] != '1':
    stack_line = file.readline()
    num_row += 1
print(num_row)

stacks_indexes = []
for i in stack_line:
    try:
        tmp = int(i)
        stacks_indexes.append(stack_line.index(i))
    except:
        continue

print(stacks_indexes)
print(num_row)

file.close()




stacks = []
for i in range(len(stacks_indexes)):
    file = open('instructions_ex.txt', 'r')
    stack = []
    stop = 0
    for j in file:
        
        try:
            if j[stacks_indexes[i]] != ' ':
                stack.append(j[stacks_indexes[i]])
        except:
            continue
        stop += 1
        if stop == num_row:
            break
    stacks.append(stack)
    file.close()

for i in stacks:
    i.reverse()
print(stacks)

moves = open('instructions.txt', 'r')

# for move in moves:
#     if move[0] == 'm':
#         quantity, init_stack, fin_stack = string_get_instructions(move)
#         for _ in range(quantity):
#             tmp = stacks[init_stack].pop()
#             stacks[fin_stack].append(tmp)
# print('########### First Half ###########')

# print('Final stacks:')
# for j in range(len(stacks)):
#     print(f"Stack_{j+1}: ", stacks[j])

# res = ''

# for crate in stacks:
#     res += crate[len(crate) - 1]
# print(res)

print('########### Second Half ###########')
for move in moves:
    if move[0] == 'm':
        quantity, init_stack, fin_stack = string_get_instructions(move)
        stacks[fin_stack] = stacks[fin_stack] + stacks[init_stack][len(stacks[init_stack]) - quantity : len(stacks[init_stack])]
        stacks[init_stack] = stacks[init_stack][0 : len(stacks[init_stack]) - quantity]

res = ''
for crate in stacks:
    res += crate[len(crate) - 1]
print(res)