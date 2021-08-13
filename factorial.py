while 1==1 :
   firstnum = int(input('Please enter your number : '))
   factorial = 1
   while firstnum >= 1 :
     factorial*=firstnum
     firstnum-=1
   print("factorial : "+str(factorial))
   print("\n"+"1) test a new number ")
   print("Else(number) : Exit")
   choice = int(input())
   if choice !=1 :
        break
print("good bye ^ _ ^")
print("author : Abtin Zandi")