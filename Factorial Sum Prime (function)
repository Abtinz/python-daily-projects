import math
def sumresualt(firstnum) :
   sumresult=0
   while firstnum >= 1 :
     sumresult+=firstnum
     firstnum-=1
   return sumresult
   
def factorial(firstnum) :
   multipyres=1
   while firstnum >= 1 :
     multipyres*=firstnum
     firstnum-=1
   return multipyres

def isprime(num) :
    if  num % 2 == 0 : 
          if num == 2 : print(str(num) + " is prime !")
          else : print(str(num) + " is not prime !")
    else :
        i=3
        isprime = 0
        while i <= math.sqrt(num) :
          if  num % i == 0 :
              isprime = 1
              break
          else : i-=-2
        if isprime == 1 : print(str(num) + " is not prime !")
        else : print(str(num) + " is prime !")
def mainmenu() :
    while 1==1 :
        firstnum = int(input('Please enter your number : '))
        print("sum resualt : "+str(sumresualt(firstnum)))
        print("factorial resualt : "+str(factorial(firstnum)))
        print(f"prime situation of {firstnum} :" , end=" ")
        isprime(firstnum)
        print("\n"+"1) test a new name ")
        print("any key : Exit")
        choice = input()
        if choice !="1" :
            break
    print("good bye ^ _ ^")
mainmenu()
