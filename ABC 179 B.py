n = int(input())
d = []
for i in range(n):
    d1,d2 = map(int, input().split())
    d.append([d1,d2])

cnt = 0
for i in range(n-2):
    if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
        print("Yes")
        exit()
print("No")