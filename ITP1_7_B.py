TF = True
while TF:
    n,x = map(int,input().split())
    if n == 0:
        TF = False
        continue
    cnt = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                if i + j + k == x:
                    cnt += 1
    print(cnt)