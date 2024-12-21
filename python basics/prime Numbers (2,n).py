import math
def isprime (number) :
  isprime = True
  if  number % 2 == 0 and number !=2: isprime=False
  else :
      i=3
      while i <= math.sqrt(number) :
          if  number % i == 0 :
              isprime = False
              break
          else : i-=-2

      if isprime : print(str(number) + " is prime !")
   

def main():
  while 1==1 : 
    number = int(input('Please enter your number : '))
    while(number >1) :
      isprime(number)
      number-=1
    print("1) new number")
    print("else keyboard : Exit")
    choice = input()
    if choice != '1':break 

  print("good bye ^ _ ^")

main()