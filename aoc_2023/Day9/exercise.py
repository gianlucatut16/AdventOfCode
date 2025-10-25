import turtle

def distance(tails : list, heads : list):
    head = heads[- 1]
    tail = tails[- 1]
    if tail[0] - head[0] == 2:
        if tail[1] == head[1]:
            new_t = (tail[0] - 1, tail[1])

        elif head[1] > tail[1]:
            new_t = (tail[0] - 1, tail[1] + 1)
        
        else:
            new_t = (tail[0] - 1, tail[1] - 1)
    elif head[0] - tail[0] == 2:
        if tail[1] == head[1]:
            new_t = (tail[0] + 1, tail[1])

        elif head[1] > tail[1]:
            new_t = (tail[0] + 1, tail[1] + 1)
        
        else:
            new_t = (tail[0] + 1, tail[1] - 1)
    elif head[1] - tail[1] == 2:
        if head[0] == tail[0]:
            new_t = (tail[0], tail[1] + 1)
        elif head[0] > tail[0]:
            new_t = (tail[0] + 1, tail[1] + 1)
        else:
            new_t = (tail[0] - 1, tail[1] + 1)
    elif tail[1] - head[1] == 2:
        if head[0] == tail[0]:
            new_t = (tail[0], tail[1] -1)
        elif head[0] > tail[0]:
            new_t = (tail[0] + 1, tail[1] - 1)
        else:
            new_t = (tail[0] - 1, tail[1] - 1)

    
    elif tail[1] - head[1] <= 1 and tail[0] - head[0] <= 1:
        new_t = tail
    

    tails.append(new_t)

def distinct_list(list):
    distinct = []
    for _ in list:
        if _ not in distinct:
            distinct.append(_)
    return distinct


file = open('input.txt', 'r')

rope = []
for i in range(10):
    rope.append([(0,0)])


for line in file:

    line_split = line.split()
    module = int(line_split[1])
    direction = line_split[0]
    for j in range(1, module + 1):
        prev = rope[0][len(rope[0]) -  1]
        if direction == 'R':
            head = (prev[0] + 1, prev[1])
        elif direction == 'L':
            head = (prev[0] - 1, prev[1])
        elif direction == 'U':
            head = (prev[0], prev[1] + 1)
        else:
            head = (prev[0], prev[1] - 1)
        
        rope[0].append(head)
        for j in range(1, 10):
            distance(rope[j], rope[j - 1])


distinct_1 = distinct_list(rope[1])
distinct_9 = distinct_list(rope[9])

print(len(distinct_1), len(distinct_9))


print(len(rope[1]))


wn = turtle.Screen()
a,b,c,d,e,f,g,h,i,l = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
johns = [a,b,c,d,e,f,g,h,i,l]
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'black','red', 'blue', 'green', 'yellow', 'purple']
for i in range(10):
    johns[i].color(colors[i])
turtle.speed(0)
for j in range(len(rope[0])):
    for i in range(10):
        johns[i].setx(rope[i][j][0]*5)
        johns[i].sety(rope[i][j][1]*5)
    
wn.exitonclick()

