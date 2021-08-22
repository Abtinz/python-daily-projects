### speed tuples > lists
informationtuples  = ("Abtin","Zandi","19","Tehran","AUT","09102266022","persian")
print(informationtuples)
print(type(informationtuples))
print("tuples are unchangable")
### tuples --> list(cast)
informationtuples=list(informationtuples)
print(informationtuples)
print(type(informationtuples))
###  list --> tuples(cast)
informationtuples=tuple(informationtuples)
print(informationtuples)
print(type(informationtuples))

### tuple + tuple
skillstuples =("python","C","HTML.CSS","JAVA")
new_tuple = skillstuples + informationtuples
print(new_tuple)
print(type(new_tuple))

