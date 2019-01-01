first_day, second_day = [], []
for i in range(3):
    first_day.append(int(input()))

for i in range(3):
    second_day.append(int(input()))

diff = 0
for i, sec in zip(range(3), [3600, 60, 1]):
    diff += (second_day[i] - first_day[i]) * sec

print(diff)
