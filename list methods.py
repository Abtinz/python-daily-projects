informationlist = ["Abtin","Zandi","19","Tehran","AUT","09102266022","persian"]

print(informationlist)
print(len(informationlist))

### insert (index,new member)
print("insert method")
informationlist.insert(3,"Hamedan")
print(informationlist)
print(len(informationlist))

### remove(removed member)
print("remove method")
informationlist.remove("Tehran")
print(informationlist)
print(len(informationlist))

### append
print("addend method")
informationlist.append("male")
print(informationlist)
print(len(informationlist))


### extend
print("extend method")
skills_list =["python","C","HTML.CSS","JAVA"]
informationlist.extend(skills_list)
print(informationlist)
print(len(informationlist))

### tupel ...
### its like list 
### but you cant edit any index here
sklist = ("python","C","JAVA","HTML.CSS")

### pop 
print("pop method")
informationlist.pop(7)
print(informationlist)
print(len(informationlist))

### if you want to remove last index pop()
print("pop() method")
informationlist.pop()
print(informationlist)
print(len(informationlist))

### del ...
print("del")
del informationlist[5]
print(informationlist)
print(len(informationlist))

### del frindes -> []

### sort
print("sort method")
informationlist.sort()
print(informationlist)
print(len(informationlist))
### upper case > lower case

### sort revers
print("sort revers method")
informationlist.sort(reverse=True)
print(informationlist)
print(len(informationlist))

### copy
print("copy method")
newlist=informationlist.copy()
print(newlist)
print(len(newlist))

### join list
print("join list")
newlist=skills_list+informationlist
print(newlist)
print(len(newlist))
