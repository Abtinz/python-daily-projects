informationset = {"Abtin","Zandi","19","Tehran","AUT","09102266022","persian","Abtin"}
skillsset ={"python","C","HTML.CSS","JAVA"}
print("sets are unorderd and unindexed and unchangable")
print("all items are uniqe ...")
print(informationset)
print(len(informationset))
### search (in)... 
### casesensetive
print("Abtin" in  informationset)

### add set
print("add set method")
informationset.add("Iran")
print(informationset)
print(len(informationset))

### update set
print("update set method")
informationset.update(skillsset)
print(informationset)
print(len(informationset))

### remove set
print("remove set method")
informationset.remove("Tehran")
informationset.add("Hamedan")
print(informationset)
print(len(informationset))

### discard set
print("discard set method (error free)")
informationset.discard("09102266022")
print(informationset)
print(len(informationset))

### pop set (random)
print("pop set method (random)")
informationset.pop()
print(informationset)
print(len(informationset))

### clear method -> {} (error free)
### del method -->  print-->error

### join two set
### union set
print("union set method")
newskillset={"PHP","JS","C++","C#","python"}
allset=newskillset.union(skillsset)
print(allset)
print(len(allset))

### intersection set
print("intersection set method")
newskillset1=newskillset.intersection(skillsset)
print(newskillset1)
print(len(newskillset1))

### intersection_update set
print("intersection_update set method")
newskillset2={"Fire Fox","microsoft office","windose","python"}
newskillset2.intersection_update(skillsset)
print(newskillset2)
print(len(newskillset2))

### symmetric_difference set
print("symmetric_difference set method")
newskillset1=newskillset.symmetric_difference(skillsset)
print(newskillset1)
print(len(newskillset1))

### symmetric_difference_update set
print("symmetric_difference_update method")
newskillset.symmetric_difference_update(skillsset)
print(newskillset)
print(len(newskillset))

print(skillsset | newskillset)
print(skillsset & newskillset)
