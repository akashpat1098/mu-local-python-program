def fib_recurse(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_recurse(n-1)+fib_recurse(n-2)
def fib_iterate(n):
    a,b=0,1
    for i in range(1,n):
        a,b=b,a+b
    return a
    # pass the index as argument
print(fib_recurse(1)) 
print(fib_iterate(1))