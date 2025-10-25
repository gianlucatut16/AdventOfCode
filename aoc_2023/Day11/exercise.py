import math

file = open('input.txt', 'r')
monkeys = []
operations = []
divisible = []
trues, falses = [], []

for line in file:
    line_spl = line.split()
    if line_spl == []:
        continue
    else:
        if len(line_spl) == 2:
            monkeys.append([])
        else:
            if line_spl[0] == 'Starting':
                for j in range(2, len(line_spl)):
                    monkeys[-1].append(int(line_spl[j][0:2]))
            elif line_spl[0] == 'Operation:':
                try:
                    operations.append((line_spl[-2], int(line_spl[-1])))
                except:
                    operations.append((line_spl[-2], line_spl[-1]))
            elif line_spl[0] == 'Test:':
                divisible.append(int(line_spl[-1]))
            elif line_spl[1] == 'true:':
                trues.append(int(line_spl[-1]))
            elif line_spl[1] == 'false:':
                falses.append(int(line_spl[-1]))
        
counters= [0 for i in range(len(monkeys))]
print(counters)
print(monkeys)

limit = math.lcm(*divisible)

for _ in range(10000):
    print(_)
    for j in range(len(monkeys)):
        
        monkey = monkeys[j]        
        to_remove = len(monkey)
        counters[j] += to_remove
        operation = operations[j]
        divisor = divisible[j]
        mon_true = trues[j]
        mon_false = falses[j]

        for worry in monkey:
            if operation[0] == '*':
                if operation[1] != 'old':
                    worry *= operation[1]
                else:
                    worry *= worry
            else:
                worry += operation[1]
            
            if worry > limit:
                worry %= limit
                
            if worry % divisor == 0:
                monkeys[mon_true].append(worry)
            else:
                monkeys[mon_false].append(worry)
        monkeys[j] = monkeys[j][to_remove :]

counters.sort()
print(counters[-1] * counters[-2])
