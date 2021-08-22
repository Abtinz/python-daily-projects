name="abtin"
lastname = "zandi"
nation="persian"
country="iran"
age=19
city="Tehran"
print(name + "\n" + lastname + "\n" + nation+ "\t"+ country)
text="""hello
im abtin
im form iran"""
print("\n" +text)

### index
print(name[0]+"\n"+name[-1])
print("\n"+lastname[1:4])

NAME=name+lastname
head="student information :"
txt=f"name : {name}\nlast name : {lastname}\nnation : {nation}\ncity :{city}\nage :{age}"
print(head)
print(txt)
print(name.capitalize())
print(lastname.casefold())
print(txt.count(" "))
print(txt.find("abtin"))
print(txt.index("ab"))

