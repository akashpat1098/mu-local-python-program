import requests
import pickle
# req iris data as response obj
iris_data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# convert iris response obj into json striing
iris_json=iris_data.text
# converting json string into list by slitting from \n
iris_list_data=iris_json.split("\n")

file="iris_pickel.pkl"
# opening above file for pickling the iris list data
with open(file,"wb") as file_obj:
    # take two arg- 1 is obj t which pickel is to be done,2 is file obj to which pickel has to store
    pickle.dump(iris_list_data,file_obj)
# opening above file for reading from pickel data of iris
with open(file,"rb") as fileobj:
    iris_data=pickle.load(fileobj)#type of object is also intake with it so it will retain its type of previous
    for data in iris_data:
        print(data.strip())
