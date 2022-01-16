
# method for getting dates
def getdate():
    import datetime
    return datetime.datetime.now()
# method for setting diet of client
def setdiet(client,diet):
    client.write(str([str(getdate())])+":"+diet+"\n")
    print("Added Succesfully")
# method for getting diet of client 
def getdiet(client):
    return client.readline()
# method for setting exercise of client
def setExercise(client,exercise):
    client.write(str([str(getdate())])+":"+exercise+"\n")
    print("Added Succesfully")
# method for getting exercise of client
def getExercise(client):
    return client.readline()

client=int(input('''Enter 1-Akash 2-Saurabh 3-Nitesh:'''))
Query=int(input('''Enter the Query 1-Diet 2-Exercise:'''))

if(Query==1):
    info=int(input('''Enter 1-Setting Diet 2-Display Diet:'''))
    if(info==1):
        diet=input("Enter the name of Diet:")

elif(Query==2):
    info=int(input('''Enter 1-Setting Exercise 2-Display Exercise:'''))
    if(info==1):
        exercise=input("Enter the name of Exercise:")
else:
    print('Wrong Input')
if Query==1: #for diet
    if info==1: #Setting values
        if client==1: #Akash
            with open("Akash_diet.txt","a") as Akash_diet:
                setdiet(Akash_diet,diet)
        elif client==2: #Saurabh
            with open("Saurabh_diet.txt","a") as Saurabh_diet:
                setdiet(Saurabh_diet,diet)
        elif client==3: #Nitesh
            with open("Nitesh_diet.txt","a") as Nitesh_diet:
                setdiet(Nitesh_diet,diet)
    elif info==2: #Displaying Values
        if client==1: #Akash
            with open("Akash_diet.txt") as Akash_diet:
                print(getdiet(Akash_diet))
        elif client==2: #Saurabh
            with open("Saurabh_diet.txt") as Saurabh_diet:
                print(getdiet(Saurabh_diet))
        elif client==3: #Nitesh
            with open("Nitesh_diet.txt") as Nitesh_diet:
                print(getdiet(Nitesh_diet))
elif Query==2: #for Exercise
    if info==1: #For setting
        if client==1: #Akash
            with open("Akash_exrcise.txt","a") as Akash_exrcise:
                setExercise(Akash_exrcise,exercise)
        elif client==2: #Saurabh
            with open("Saurabh_exrcise.txt","a") as Saurabh_exrcise:    
                setExercise(Saurabh_exrcise,exercise)
        elif client==3: #Nitesh
            with open("Nitesh_exrcise.txt","a") as Nitesh_exrcise:
                setExercise(Nitesh_exrcise,exercise)
    elif info==2: #For Displaying
        if client==1: #Akash
            with open("Akash_exrcise.txt") as Akash_exrcise:
                print(getExercise(Akash_exrcise))
        elif client==2: #Saurabh
            with open("Saurabh_exrcise.txt") as Saurabh_exrcise:    
                print(getExercise(Saurabh_exrcise))
        elif client==3: #Nitesh
            with open("Nitesh_exrcise.txt") as Nitesh_exrcise:
                    print(getExercise(Nitesh_exrcise))

                


    




