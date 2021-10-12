def Sum(num1, num2):
    print(f"a + b ={num1+num2}")

def Minus(num1, num2):
    print(f"a - b ={num1-num2}")

def multiplication(num1, num2):
    print(f"a * b ={num1*num2}")

def Division(num1, num2):
    print(f"a / b ={num1/num2}")

def Percentage(num1, num2):
    print(f"a % b ={num1%num2}")

def main_menu():
    print("welcomt to calcuator : ")
    print("please enter first number :")
    num1 = int(input())
    print("please enter second number :")
    num2 = int(input())
    while 1 == 1:
        print("1) Sum(num1,num2)")
        print("2) Minus(num1,num2)")
        print("3) Multiplication(num1,num2)")
        print("4) Division(num1,num2)")
        print("5) Percentage(num1,num2)")
        print("6) All available operators(num1,num2)")
        print("Else(number) : Exit")
        choice = int(input())
        if choice == 1:
            Sum(num1, num2)
        elif choice == 2:
            Minus(num1, num2)
        elif choice == 3:
           multiplication(num1, num2)
        elif choice == 4:
           Division(num1, num2)
        elif choice == 5:
           Percentage(num1, num2)
        elif choice == 6:
           Sum(num1, num2)
           Minus(num1, num2)
           multiplication(num1, num2)
           Division(num1, num2)
           Percentage(num1, num2)
        else:
           print("good bye ^ _ ^")
           break

main_menu()
