def printAlphaba(rowNumber) :
    asciiNum = 65
    for i in range(0,rowNumber) :
      for j in range(0,i+1) :
          character = chr(asciiNum)
          print(character,end=" ")
          asciiNum-=-1
      print("\r")
number = int(input('please enter the number of alphabas : '))
printAlphaba(number)
