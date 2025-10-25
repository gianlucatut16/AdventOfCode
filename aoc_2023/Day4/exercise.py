comps = open('input.txt', 'r')
sum = 1000
i = 1
for ranges in comps:
    ranges = ranges.split(',')
    a = ranges[0].split('-')
    b = ranges[1].split('-')
    a_1 = int(a[0])
    b_1 = int(a[1])
    a_2 = int(b[0])
    b_2 = int(b[1])
    if (b_1 < a_2) or (b_2 < a_1) or (a_1 > b_2) or (a_2 > b_1):
            sum -= 1
    
print(sum)