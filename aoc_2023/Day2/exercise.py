def result_round(round):
    if round in draws:
        result = 3
    elif round in wins:
        result = 6
    else:
        result = 0
    return result

def result_shape(shape):   
    if shape == 'X':
        shape = 1
    elif shape == 'Y':
        shape = 2
    else:
        shape = 3
    return shape

rounds = open('values.txt', 'r')
# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors

# X = lose, Y = draw, Z = win
wins = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
draws = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
losses = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]
sum = 0

print('################ First Half ################')

# for round in rounds:
#     round = round.split()
#     result = result_round(round)
#     my_shape = round[1]
#     shape = result_shape(my_shape)
#     sum += shape + result
    
print('################ Second Half ################')

for round in rounds:
    round = round.split()
    if round[1] == 'X':
        for x in losses:
            if round[0] in x:
                hand  = x
    elif round[1] == 'Y':
        for x in draws:
            if round[0] in x:
                hand  = x
    else:
        for x in wins:
            if round[0] in x:
                hand  = x
    
    result = result_round(hand)
    my_shape = hand[1]
    shape = result_shape(my_shape)
    sum += shape + result
print(sum)

