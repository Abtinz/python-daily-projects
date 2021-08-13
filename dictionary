information = {
    "name": "Abtin",
    "last_name": "Zandi",
    "age": "19",
    "city": "Tehran",
    "city": "Hamedan",
    "nation": "persian",
    "university": "AUT",
    "phone_number": "091022066022",
    "skills": ["HTML and CSS", "Python", "Jave", "C"]
    # key value saved
}
print(information)
print(len(information))
print(type(information))

# acces
print("how to acces")
# simple
name = information['name']
print(name)

# get method
print("get method")
lastname = information.get('last_name')
print(lastname)

# key method
print("key method --> printing all keys")
allkeys = information.keys()
print(allkeys)

# values method
print("value method --> printing all values")
allvalues = information.values()
print(allvalues)

# item method
print("item method --> (key,value)")
item = information.items()
print(item)

# change or add new item
information["city"] = "Toronto"
print(information)

# update method
print("update method (change or add)")
information.update({"skills": ["HTML", "Python", "C"]})
information.update({"grade": 19})
print(information)
print(len(information))

# remove item
# pop method
print("pop method (key)")
print("pop() --> error")
information.pop("phone_number")
print(information)
print(len(information))

# popitem method
print("popitem method == pop() in list"+"\n"+"<< last item>>")
information.popitem()
print(information)
print(len(information))

# clear method --> {}

# copy dicts
# copy method
print("copy method")
newinfodict = information.copy()
newinfodict["freind"] = "arya"
print(newinfodict)

# dict method
print("dict method")
newinfodict2 = dict(newinfodict)
print(newinfodict2)
