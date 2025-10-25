file = open('input.txt', 'r')

rows = []
for i in file:
    try:
        rows.append([int(j) for j in list(i)])
    except:
        rows.append([int(j) for j in list(i[:len(i)-1])])


columns = []
for i in range(len(rows[0])):
    columns.append([t[i] for t in rows])


sum = 0
for i in range(1, len(rows) - 1):
    for j in range(1,len(rows)-1):
        if rows[i][j] > max(rows[i][j+1:]) or rows[i][j] > max(rows[i][:j]) or rows[i][j] > max(columns[j][i+1:]) or rows[i][j] > max(columns[j][:i]):
                sum+= 1

print('**************** First part ****************')
print(sum + 2 * len(rows) + 2 * (len(columns) - 2))
products = []

for i in range(1, len(rows) - 1):
    for j in range(1,len(rows)-1):
        prod = 1
        tree  = rows[i][j]
        #looking right
        right_trees = rows[i][j + 1:]
        for z in range(len(right_trees)):
            if right_trees[z] >= tree:
                prod *= z + 1
                break
            elif z == len(right_trees) - 1:
                prod *= len(right_trees)


        #looking left
        left_trees = rows[i][:j]
        left_trees.reverse()
        for z in range(len(left_trees)):
            if left_trees[z] >= tree:
                prod *= z + 1
                break
            elif z == len(left_trees) - 1:
                prod *= len(left_trees)

        #looking up
        up_trees = columns[j][:i]
        up_trees.reverse()
        for z in range(len(up_trees)):
            if up_trees[z] >= tree:
                prod *= z + 1
                break
            elif z == len(up_trees) - 1:
                prod *= len(up_trees)
                
        # looking down
        down_trees = columns[j][i + 1:]
        for z in range(len(down_trees)):
            if down_trees[z] >= tree:
                prod *= z + 1
                break
            elif z == len(down_trees) - 1:
                prod *= len(down_trees)
            
        products.append(prod)

print('**************** Second part ****************')
print(max(products))