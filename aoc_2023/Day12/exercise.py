file = open('input.txt', 'r')


def to_numbers(rows):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(rows)):
        rows[i] = list(rows[i])
        for j in range(len(rows[i])):
            if rows[i][j] in alphabet:
                rows[i][j] = alphabet.index(rows[i][j]) + 1
            else:
                continue
    return rows

def path(rows, sum, i, j):
    finish = False
    position = rows[i][j]
    
    

    return finish, 

rows = []
line = file.readline()
i=1
while i<5:
    rows.append(line[:len(line) - 1])
    line = file.readline()
    i+=1
rows.append(line)




columns = []

num_column = len(rows[0])
num_rows = len(rows)

for z in range(num_column):
    string = ''
    for i in rows:
        string += i[z]
    columns.append(string)
    


rows = to_numbers(rows)
columns = to_numbers(columns)
for i in rows:
    print(i)

i,j = 0, 0
for i in range(num_rows):
    for j in range(num_column):
        try:
            if rows[i][j] > rows[i][j + 1] - 1:
                rows[i][j+1] = '.'
            elif rows[i][j] > rows[i][j - 1] - 1:
                rows[i][j - 1] = '.'
            elif rows[i][j] > rows[i+1][j] - 1:
                rows[i+1][j] = '.'
            elif rows[i][j] > rows[i-1][j] - 1: