a,b=map(int,input().split())
for i in range(-1000,1000):
    for j in range(-1000,1000):
        if (i+j)==a and (i-j)==b:
            print(i,j)
            exit()