def sqrtcode (number) :
      originalNumber = number
      prime = []
      powOfNumbers = []
      finalNumbers = []
      result = 1
      if  number % 2 == 0 : 
          prime.append(2)
          powNum=0
          while number % 2 == 0 : 
             number/= 2
             powNum-=-1
          powOfNumbers.append(powNum)
          finalNumbers.append(1)
      number=int(number)
      i=3
      while i <= number :
          if  number % i == 0 :
              if isprime(i) : 
                  prime.append(i)
                  powNum=0
                  while number % i == 0 : 
                     number/= i
                     powNum-=-1
                  powOfNumbers.append(powNum)
                  finalNumbers.append(1)
          i-=-2
 
      index = 0
      while index <len(powOfNumbers) :
          n=0
          while n < powOfNumbers[index] :
            finalNumbers[index] *= prime[index]
            n-=-1
          index-=-1
      index = 0
      while index <len(finalNumbers) :
            finalNumbers[index] = finalNumbers[index] ** 0.5
            index-=-1
      finalNumber = 1
      index = 0
      while index <len(finalNumbers) :
            finalNumber *= finalNumbers[index] 
            index-=-1
      print("SQRT of "+str(originalNumber)+" is : \n"+str(finalNumber))



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
    sqrtcode(number)
    print("----------------------")
    print("1) new number")
    print("else keyboard : Exit")
    choice = input()
    if choice != '1': break 

  print("good bye ^ _ ^")
  
main()
