#Enter Input
n = int(input())
primes = [1 for i in range(n + 1)]
primes[0], primes[1] = 0, 0

current = 2
while (current * current <= n):
    if primes[current] == 1:
        for i in range(current * 2, n + 1, current):
            primes[i] = 0
    current += 1

#Print numbers
for i in range(2, n):
    if (primes[i] == 1):
        print(i)