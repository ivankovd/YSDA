n = int(input())

max_10 = n // 10

ans = 0

for i_10 in range(max_10 + 1):
    after_10 = n - i_10 * 10
    ans += after_10 // 5 + 1

print(ans)
