def splitting(string):
    return string.split('-')

num = 0
num1 = 0

file = open('input.txt', 'r')
for line in file:
    line_split = line.split(',')
    line_list = []
    for i in line_split:
        line_list += splitting(i)
    a1, b1, a2, b2 = int(line_list[0]), int(line_list[1]), int(line_list[2]), int(line_list[3])
    if a1 <= a2 and b1 >= b2:
        num += 1
    elif a2 <= a1 and b2 >= b1:
        num += 1
    
    list1 = list(range(a1, b1 + 1))
    list2 = list(range(a2, b2 + 1))
    for j in list1:
        if j in list2:
            num1 += 1
            break
print(f'-- First part --\n{num}\n-- Second part --\n{num1}')