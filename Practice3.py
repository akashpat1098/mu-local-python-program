from matplotlib.pyplot import flag


foods=[]
size=int(input("Enter the size of list:"))
print("Enter the numbers of list one by one:")
for i in range(size):
    foods.append(int(input()))

foods.sort(reverse=True)
print(f"The given list is:{foods}")
# method 1
reverse1=foods[:]
reverse1.reverse()
print(f"The reverse list is{reverse1}")

# method 2
reverse2=foods[:]
print(f"The reverse list is{reverse2[::-1]}")

# method 3
reverse3=foods[:]
for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3)-1-i]=reverse3[len(reverse3)-1-i],reverse3[i]
print(f"The reverse list is{reverse3}")


