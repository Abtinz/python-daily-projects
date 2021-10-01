import moudle 
def main():
  while 1==1 : 
    number = int(input('Please enter your number : '))
    print("----------------------")
    moudle.sqrtcode(number)
    print("----------------------")
    print("1) new number")
    print("else keyboard : Exit")
    choice = input()
    if choice != '1': break 

  print("good bye ^ _ ^")
  
main()