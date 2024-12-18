my_dict={"std_id":123,"name":"abc","course":"mca"}
print(my_dict)

x=my_dict["course"]
print("The course selected is",x)

x=my_dict.get("std_id")
print(x)

#find all the keys present in the dictionary
y=my_dict.keys()
print("Thekeys present are :",y)

#to update
my_dict.update({"name":"xyz"})
print(my_dict)

#to add new element
my_dict["fess"]=76000
print(my_dict)

#to remove certain item
my_dict.popitem()
print(my_dict)

my_dict.pop("name")
print(my_dict)

#looping over dictionary
for i in my_dict:
    print(i)


#to GET keys from the dictionary
for i in my_dict.keys():
    print(i)

# to get values from the lis
for i in my_dict.values():
    print(i)

for x,y in my_dict.items():
    print(x,y)
