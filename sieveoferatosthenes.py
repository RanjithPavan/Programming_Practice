from math import sqrt

for t in range(int(input())):
    start, end = map(int,input().split())
    primes = {}
    for num in range(2, int(sqrt(end)+1)):
        for otherNum in range(max(2, start //num), ((end // num)+1)):
            primes[num * otherNum] = 0
    for num in range(max(2, start), (end+1)):
        if num not in primes:
            print(num)
    print()
