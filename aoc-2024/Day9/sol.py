import numpy as np

def check_row(row):
    # Decreasing
    check = True
    if row[1] in range(row[0]-3, row[0]):
        for i in range(2, len(row)):
            curr_num = row[i]
            prec = row[i - 1]
            if curr_num not in range(prec - 3, prec):
                problematic_index = i
                check = False
    # Increasing order
    elif row[1] in range(row[0] + 1, row[0] + 4):
        for i in range(2, len(row)):
            curr_num = row[i]
            prec = row[i - 1]
            if curr_num not in range(prec + 1, prec + 4):
                problematic_index = i
                check = False

    elif row[1] not in range(row[0] - 3, row[0] + 4) or row[1] == row[0]:
        problematic_index = 1
        check = False

    if check == False:
        return check, problematic_index
    else:
        return check, None
    



check_lst = []
with open('real_input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        row = [int(char) for char in line.split(' ')]

        check_0, problematic_index = check_row(row)
    
        if check_0 == False:
            for ind in range(len(row)):
                new_row = [row[i] for i in range(len(row)) if i != ind]
                check_1, problematic_index_ = check_row(new_row)
                if check_1 == True:
                    check_0 = True
                    break



        check_lst.append(check_0)
        

    print(np.sum(check_lst))


