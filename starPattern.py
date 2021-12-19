# Left-triangular star pattern
rows=int(input("Enter the no of rows"))
i=1
while(i<=rows):
    j=1
    while(j<=i):
        print("*",end="")
        j=j+1
    i=i+1
    print("")

# right triangular star pattern
# ye wala pyramidal bhi print kr rha h agr star ke baad space daale toh

rows=int(input("Enter the no of rows"))
i=1
while(i<=rows):
    j=1
    while(j<=rows-i):
        print("  ",end="")
        j=j+1
    k=1
    while(k<=i):
        print("* ",end="")
        k=k+1
    print("")
    i=i+1
        


