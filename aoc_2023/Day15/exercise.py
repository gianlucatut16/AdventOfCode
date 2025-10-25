import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


def man_distance(coord_1 : tuple, coord_2 : tuple):
    distance = abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])
    return distance

file = open('input.txt', 'r')
sensors = []
beacons = []

for i in file:
    x_s = i.split()[2]
    y_s = i.split()[3]
    x_b = i.split()[-2]
    y_b = i.split()[-1]
    sensors.append((int(x_s[2:len(x_s)-1]), int(y_s[2:len(y_s)-1])))
    beacons.append((int(x_b[2:len(x_b)-1]), int(y_b[2:len(y_b)])))

# # Visualization

# plt.scatter(x_sensors, y_sensors)
# plt.scatter(x_beacons, y_beacons)
# plt.show()

distance_sensors_beacons = []

for i in range(len(sensors)):
    distance_sensors_beacons.append(man_distance(sensors[i], beacons[i]))

print(distance_sensors_beacons)

total_not = []

y = 2000000

x_limit_down = []
x_limit_up = []
for i in range(len(sensors)):
    tmp_min = sensors[i][0] - distance_sensors_beacons[i]
    x_limit_down.append(tmp_min)
    tmp_max = sensors[i][0] + distance_sensors_beacons[i]
    x_limit_up.append(tmp_max)


x_beacons = [i[0] for i in beacons]

if min(x_limit_down) < min(x_beacons):
    minimo = min(x_limit_down)
else:
    minimo = min(x_beacons)
    
if max(x_limit_up) > max(x_beacons):
    massimo = max(x_limit_up)
else:
    massimo = max(x_beacons)

print(massimo - minimo)
print(sensors)

sum = 0
for x in range(minimo, massimo + 1):
    coord = (x,y)
    if coord in beacons or coord in sensors:
        continue
    for i in sensors:
        if man_distance(coord, i) <= distance_sensors_beacons[sensors.index(i)]:
            sum += 1
            break
print(sum)