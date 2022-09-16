cas=int(input())
for _ in range(0,cas):
    a,b=map(int,input().split())
    if a==b:
        print("ANY")
    elif b>a:
        print("SECOND")
    else:
        print("FIRST")
