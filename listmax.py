def listMaxDuplicated(myList):
    index=0
    secondeIndex=0
    counter=0
    while index<len(myList) :
        while secondeIndex < len(myList) :
            if index != secondeIndex : 
                 if(myList[index] == myList[secondeIndex]): counter-=-1
            secondeIndex-=-1  
        
        if counter >= len(myList)/2 : 
            print(f"\"{myList[index]}\" is the most repeated item")
            break
        else : 
            index-=-1  
            counter=0

def main():
  while 1==1 : 
    myList = []
    myList.append(input('Please enter your item : '))
    print("1) New Item")
    print("else keyboard : Exit")
    choice = input()
    if choice != "1": 
        listMaxDuplicated(myList) 
        break

main()