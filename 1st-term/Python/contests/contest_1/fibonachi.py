n = int(input())

n_1 = 0
n_2 = 1
fib = 1

if n == n_1:
    fib = 0
elif n == n_2:
    fib = 1

for i in range(1, n):
    n_1, n_2 = fib, n_1
    fib = n_1 + n_2

print(fib)
