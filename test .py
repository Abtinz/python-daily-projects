
def isprime (number) :
  if  number % 2 == 0 : print(str(number) + " is not prime")
  else :
      i=3
      isprime = 0
      while i < number :
          if  number % i == 0 :
              isprime = 1
              break
          else : i-=-2

      if isprime == 1 : print(str(number) + " is not prime")
      else : print(str(number) + " is prime !")
   


def main():
  while 1==1 : 
    number = int(input('Please enter your number : '))
    isprime(number)
    print("1) new number")
    print("2)else keyboard exit")
    choice = input()
    if choice != '1':break 

  print("good bye ^ _ ^")

main()