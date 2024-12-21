import math

def primeitem (number) :
      firstNumber = number
      prime = []
      if  number % 2 == 0 : 
          prime.append(2)
          while number % 2 == 0 : 
             number/=2
      number=int(number)
      i=3
      while i <= number :
          if  number % i == 0 :
              check = isprime(i)
              if check : 
                prime.append(i)
          i-=-2
      print("Counters prime numbers of "+str(firstNumber))
      n=1
      for item in prime :
           print(str(n) + ") " +str(item))
           n-=-1
      if number == 1 : print("your number is one \nit dosent have any Counters prime numbers") 

def isprime (number) :
      i=2
      isprime = 0
      while i < number :
          if  number % i == 0 :
              isprime = 1
              break
          else : i-=-1

      if isprime != 1 : return True

def main():
  while 1==1 : 
    number = int(input('Please enter your number : '))
    print("----------------------")
    primeitem(number)
    print("----------------------")
    print("1) new number")
    print("else keyboard : Exit")
    choice = input()
    if choice != '1': break 

  print("good bye ^ _ ^")
  
main()
