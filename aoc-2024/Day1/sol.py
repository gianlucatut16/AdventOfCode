import numpy as np

input = np.loadtxt('real_input.txt')

distances_lst = []

left_lst = input[:, 0]
right_lst = input[:, 1]

srt_left = sorted(left_lst)
srt_right = sorted(right_lst)

for i in range(len(srt_left)):
    diff = abs(srt_left[i] - srt_right[i])
    distances_lst.append(diff)

print(np.sum(distances_lst))