s,t = map(int, input().split())

count = 0
for a in range(101):
    for b in range(101):
        for c in range(101):
            if (a+b+c) <= s and a*b*c <= t:
                count += 1
print(count)