n = int(input())
k = 0
if not n:
    print(-1.0)
if n < 0:
    n = -n
    q = int(n**0.5)
    if q**2 == n:
        k = -1
for i in range(1, round(n**0.5) + 1):
    if n%i == 0:
        k += 2
print(k)