# (if,elif,else) condition :
print("please enter first number")
firstNum = int(input())
print("please enter second number")
secondNum = int(input())
if firstNum > secondNum:
    print(str(firstNum) + " is bigger than " + str(secondNum))
elif firstNum < secondNum:
    print(str(firstNum) + " is lower than " + str(secondNum))
else:
    print(str(firstNum) + " equal whit " + str(secondNum))

firstNum*=10
secondNum*=8

if firstNum/6 == 10 and secondNum/9 == 8:
    print("firstNum =6" + "\n" + "secondNum=9")

elif firstNum %8 == 0 and secondNum%10 == 0 :
    print(str(firstNum) + " equal whit " + str(secondNum))

if firstNum%3==0 or secondNum %3==0 :
    print("at least on of your numbers is counted by 3 !")
