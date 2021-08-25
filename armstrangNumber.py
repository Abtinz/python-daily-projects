while 1 ==1 :
   number = int(input("please enter your   Integer number : "))
   digits_sum=0
   tempNumber=number
   digits=[]
   while tempNumber >0 :
     digit = tempNumber%10
     digits.append(digit)
     digits_sum+=digit**3
     tempNumber//=10
   if number == digits_sum : 
      print("----------------------------------------------")
      i=0
      while i < len(digits) :
          if i == len(digits) - 1 : print("("+str(digits[i]**3)+") ^ 3")
          else : print("("+str(digits[i])+") ^ 3 + ",end=" " )
          i-=-1
      i=0
      while i < len(digits) :
          if i == len(digits) - 1 : print("("+str(digits[i])+") = "+str(number))
          else : print("("+str(digits[i]**3) + ") + ",end=" " )
          i-=-1
    
      print("number "+str(number)+" is an Armstrong number")
      print("----------------------------------------------")
   else : 
      print("----------------------------------------------")
      i=0
      while i < len(digits) :
         if i == len(digits) - 1 : print("("+str(digits[i]**3)+") ^ 3")
         else : print("("+str(digits[i])+") ^ 3 + ",end=" " )
         i-=-1
      i=0
      while i < len(digits) :
         if i == len(digits) - 1 : print("("+str(digits[i])+") = "+str(digits_sum))
         else : print("("+str(digits[i]**3) + ") + ",end=" " )
         i-=-1
      print(str(digits_sum)+" != "+str(number))
      print("number "+str(number)+" isnt an Armstrong number")
      print("----------------------------------------------")
   print("1) new number")
   print("press any key to exit")
   choice = input()
   if choice !='1': break
print("good bye ^ _ ^")
