def calc_sum_last_3(num):
    return num % 10 + num // 10 % 10 + num // 100 % 10


def calc_sum_first_3(num):
    return num // 100000 + num // 10000 % 10 + num // 1000 % 10


ticket = input()

sum_ticket = sum(list(map(int, ticket[:3])))
last = int(ticket)
last_resp = []

for diff in range(last):
    low = last - diff
    hight = last + diff
    if calc_sum_last_3(low) == calc_sum_first_3(low):
        last_resp = str(low)
        break

    if calc_sum_last_3(hight) == calc_sum_first_3(hight):
        last_resp = str(hight)
        break

print(last_resp)
