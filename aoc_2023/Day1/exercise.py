values = open('values.txt', 'r')

sum = 0
elves = []

for line in values:
    try:
        sum += int(line)
    except:
        elves.append(sum)
        sum = 0
        continue

elves.append(sum)
best = max(elves)
index = elves.index(best)
print('############### First Half ###############')
print(f'Elf {index + 1} with more calories: {best} calories!')

print('############### Second Half ###############')

elves.pop(index)
second_best = max(elves)
index = elves.index(second_best)
elves.pop(index)
third_best = max(elves)

res = best + second_best + third_best
print(res)