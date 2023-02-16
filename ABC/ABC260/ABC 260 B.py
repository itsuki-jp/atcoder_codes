n, x, y, z = map(int, input().split())
a = map(int, input().split())
b = map(int, input().split())

s = list(zip(range(1, n + 1), a, b))
s.sort(key=lambda p: (-p[1], p[0]))
s[x:] = sorted(s[x:], key=lambda p: (-p[2], p[0]))
s[x + y:] = sorted(s[x + y:], key=lambda p: (-(p[1] + p[2]), p[0]))
s[:x + y + z] = sorted(s[:x + y + z], key=lambda p: p[0])

for p in s[:x + y + z]:
    print(p[0])
