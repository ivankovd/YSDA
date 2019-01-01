N = int(input())

res = []
for i in range(1, N+1):
    if i % 15 == 0:
        res.append('Fizz Buzz')
    elif i % 5 == 0:
        res.append('Buzz')
    elif i % 3 == 0:
        res.append('Fizz')
    else:
        res.append(str(i))

print(', '.join(res))
