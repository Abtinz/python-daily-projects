def counterNumber(number):
    counters=[1]
    integer=2
    lastRem=1
    while integer < number:
        if number % integer == 0 :
            counters.append(integer)
            lastRem=integer
        integer-=-1

    sum = 0
    print(f"counters : {counters}")
    for item in counters:
        sum+=item
    if sum == number : 
     for item in counters:
         if item == lastRem : print(f"{item}",end=" ")
         else : print(f"{item} +",end=" ")
        
     print(f"= {number}")
     print(f"{number} is completed !")
    else : 
           for item in counters:
              if item == lastRem : print(f"{item}",end=" ")
              else : print(f"{item} +",end=" ")
           print(f"!= {number}")
           print(f"{number} is not completed !")
    
def main():
  while 1==1 : 
    number = int(input('Please enter your number : '))
    counterNumber(number)
    print("1) new number")
    print("else keyboard : Exit")
    choice = input()
    if choice != '1':break 
  print("good bye ^ _ ^")

main()