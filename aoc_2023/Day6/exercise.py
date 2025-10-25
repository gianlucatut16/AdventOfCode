def all_different(a, num_char):
    if len(a) == num_char:
        for i in range(num_char - 1):
            for j in range(i + 1, num_char):
                if a[i] == a[j]:
                    return False
        return True
    else:
        return False

file = open('input.txt', 'r')

string = file.readline()
num_char = 4

for i in range(num_char - 1, len(string)):
    list_four_char = string[i - num_char : i]
    if all_different(list_four_char, num_char) == True:
        break
print(i)
        
