print("please enter your integer number")
gussed_number=input()
gussed_number=int(gussed_number)
first_num=int(gussed_number)
gussed_number*=2
show_num=str(gussed_number)
print("first stage : " + show_num)
gussed_number-=-8
show_num=str(gussed_number)
print("second stage : " + show_num)
gussed_number-=-first_num
show_num=str(gussed_number)
print("third stage : " + show_num)
gussed_number-=2
show_num=str(gussed_number)
print("fourth stage : " + show_num)
gussed_number/=3
gussed_number=int(gussed_number)
show_num=str(gussed_number)
print("fifth stage : " + show_num)
gussed_number-=first_num
show_num=str(gussed_number)
print("sixth stage : " + show_num)
gussed_number*=4
show_num=str(gussed_number)
print("result : " + show_num)
