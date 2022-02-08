# dictionary={"mutable":"can change","immutable":"cannot change",
#             "multitasking":"doing work at same time"}
# print("Enter the word for meaning")
# uservalue=input()
# print("The meaning of the \"",uservalue,"\"is \"", dictionary.get(uservalue),"\"")


# age=int(input("Enter the Age"))
# if age>18:
#     print("Drive")
# elif age<18:
#     print("Can't Drive")
# else:
#     print("Can't Decide")

# faulty calculator
# operator=input("Enter the Operator:")
# a=int(input("Enter Number 1:"))
# b=int(input("Enter Number 2:"))
# if operator=="+":
#     if a==56 and b==9:
#         print(77)
#     else:
#         print(a+b)

# elif operator=="-":
#     print(a-b)
# elif operator=="*":
#     if a==45 and b==3:
#         print(555)
#     else:
#         print(a*b)
# elif operator=="/":
#     if a==56 and b==6:
#         print(4)
#     else:
#         print(a/b)
# else:
#     print("Wrong Operator")


# li=("Akash",1,"Patel",55,"hello",456,"Six")
# for items in li:
#     if str(items).isnumeric() and items>6:
#         print(items)
        # 
# print(14%12)#-->2.0 float Divisible
# print(11/5)#-->2.2 float Non Divisible
# print(10/5)#-->2.2 float Divisible
# print(11.0/5.0)#-->2.2 float Non Divisible
# print(10//5)#-->2 int Divisible
# print(11//5)#-->2 int with truncate Non Divisible
# print(11.0//5.0)#-->2.0 float with truncate
# print(11.0//5)#--> 2.0 float with truncate

# f=open("prac.txt")
# content=f.read()
# print(content)

# f.close()


# f=open("prac.txt","a")
# f.write("hey wahtsup")

# # f.close()
# class employee:
# 	no_of_leaves=25
# 	def __init__(self,Name,Salary,Role) -> None:
# 		self.name=Name
# 		self.salary=Salary
# 		self.role=Role

# 	def printdetail(self):
# 		return f"{self.name} is an employee whose salary is {self.salary} and role is{self.role}"
# 	@classmethod
# 	def changeLeaves(cls,newleaves):
# 		cls.no_of_leaves=newleaves

# class player():
# 	def __init__(self,Name,Game) -> None:
# 		self.name=Name
# 		self.game=Game
# akash=employee("Akash",15000,"Instructor")
# saurabh=employee("Saurabh",14000,"Teacher")


# # print(akash.printdetail())
# akash.changeLeaves(22)
# print(akash.no_of_leaves)
# print(saurabh.no_of_leaves)


# #Example of using mutable object in constructoe not as class variable
# class repository:
# 	# package={}    #Dont use this as this will give error in using list by adding in same list of all instance
# 	def __init__(self) -> None:
# 		self.packages={}
# 	def add_package(self,package):
# 		self.packages[package.name]=package

# class package():
# 	def __init__(self,Name) -> None:
# 		self.name=Name

# vscode=package("vscode")
# git=package("Git")
# whatsapp=package("Whatsapp")

# bombSquad=package("BombSquad")
# pubg=package("pubg")
# freefire=package("freefire")

# Softwares=repository()
# Softwares.add_package(vscode)
# Softwares.add_package(git)
# Softwares.add_package(whatsapp)
# print(Softwares.packages.keys())

# folder=repository()
# folder.add_package(bombSquad)
# folder.add_package(pubg)
# folder.add_package(freefire)
# print(folder.packages.keys())

# # Regular Expression example
# import re
# mytxt='''Tata Group is an Indian multinational conglomerate headquartered in Mumbai.
# Founded in 1868 by Jamshedji Tata, the group gained international recognition after purchasing several global companies.
# It is one of the biggest and oldest industrial groups in India.
# Wikipedia
# Founder: Jamsetji Tata
# Founded: 1868, Mumbai
# Headquarters: Mumbai
# Customer service: 022 6665 8282
# Subsidiaries: Tata Motors, Tata Steel Ltd, MORE
# Parent organization: Tata Sons
# '''
# for i in re.findall(r"",mytxt):
# 	print(i+" ",end="")

