user_information = {
    "name": "",
    "last_name": "",
    "age": "",
    "city": "",
    "nation": "",
    "university": "",
    "phone_number": "",
    "skills": []
}

user_login = {
    "username" : "",
    "password" : ""
}
informationkey = ["name","last_name","age","city","nation","university","phone_number","skills"]
print("welcome !"+"\n"+"please enter your informations :")
print("personal information")
print("1) Name :")
user_information['name']= input()
print("2) Last_name :")
user_information['last_name']=input()
print("3) Age :")
user_information['age']=input()
print("4) Nation :")
user_information['nation']=input()
print("5) City :")
user_information['city']=input()
print("6) University :")
user_information['university']=input()
print("7) Phone_number :")
user_information['phone_number']=input()
while 1 == 1 :
   print("8) Skills :")
   user_information['skills'].append(input())
   print("do you want to enter other skill ?") 
   print("1) yes")
   print("etc. no") 
   choice = input()
   choice = int(choice)
   if choice != 1 :
       break   
print("log in informations :")
print("User name")
user_login['username']=input()
print("Password")
user_login['password']=input()
while 1==1 :
    print("please enter your password again :")
    password1=input()
    if password1 in user_login['password'] :
        break
    else :
        print("its wrong !")
 
print("you signed up succesfully !")
print("log in :")
while 1==1 :
    print("User name :")
    loginUsername=input()
    if loginUsername in user_login['username'] :
        break
    else :
        print("its wrong !")
while 1==1 :
    print("password :")
    loginPassword=input()
    if loginPassword in user_login['password'] :
        break
    else :
        print("its wrong !")
print("1) information list :")
print("2) change item :")
print("etc. Exit")
choice1 = int(input())
if choice1 == 1 :
  print("1) name :"+str(user_information['name']))
  print("2) last_name :"+str(user_information['last_name']))
  print("3) age :"+str(user_information['age']))
  print("4) city  :"+str(user_information['city']))
  print("5) nation :" + str(user_information['nation']))
  print("6) phone_number :"+str(user_information['phone_number']))
  print("7) university :"+str(user_information['university']))
  print("8) skills :"+str(user_information['skills']))
elif choice1 == 2 :
  i=0
  while i <=len(informationkey) :
       print(str(i+1) +")" + informationkey[i])
       i-=-1 
       if i == len(informationkey) :
        break
  while 1==1 :
    print("which one do you prefer to change ?(name of key)")
    change=input()
    if change in user_information.keys() :
        print("please enter your new information :")
        user_information[change]=input()
        print("user information has been changed !")
        print("new info :"+str(user_information[change]))
        break
    else :
           print("its wrong !")
  print("1) name :"+str(user_information['name']))
  print("2) last_name :"+str(user_information['last_name']))
  print("3) age :"+str(user_information['age']))
  print("4) city  :"+str(user_information['city']))
  print("5) nation :" + str(user_information['nation']))
  print("6) phone_number :"+str(user_information['phone_number']))
  print("7) university :"+str(user_information['university']))
  print("8) skills :"+str(user_information['skills']))
else :
    print("good bye ^ _ ^")
   
