backpacks = open('input.txt', 'r')
sum = 0
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# print('################ First Half ################')
# for line in backpacks:
#     first_half = line[0 : len(line)//2]
#     second_half = line[len(line)//2: len(line)]
#     for letter in first_half:
#         if letter in second_half:
#             print(letter)
#             sum += alphabet.index(letter) + 1
#             break
# print(sum)

print('################ Second Half ################')

group = []
for line in backpacks:
    group.append(line)
    if len(group) == 3:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                sum += alphabet.index(char) + 1
                group = []
                break
print(sum)


