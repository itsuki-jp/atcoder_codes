k, s = map(int, input().split())

# こっから下はパクった(-_-;)

cnt = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if k >= z >= 0:
            cnt += 1

print("{}".format(cnt))
