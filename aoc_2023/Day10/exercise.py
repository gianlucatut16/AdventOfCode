file = open('input.txt', 'r')
x_list = [1]
for line in file:
    if line.split()[0] == 'noop':
        x_list.append(x_list[-1])
    else:
        prev = x_list[-1]
        add = int(line.split()[1])
        x_list.append(prev)
        x_list.append(prev + add)
sum = 0
index = 20
for j in range(1,7):
    prod = index * x_list[index-1]
    sum += prod
    index += 40
print('*************************** First Part ***************************')    
print(sum)
