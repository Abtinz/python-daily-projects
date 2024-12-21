import re

def fifty_most_common_passwords_set(password):
    with open('password evaluation\common_passwords.txt', 'r') as file:
        for common_password in file:
            if password == common_password.strip(): return True
    return False

def is_password_strength_enough(password):
    security_amount = 0
    if len(password) > 8: 
        security_amount = 50
    else: 
        print("Password length should be at least 8 characters.(you lost 50/100 of your security in brute force attack)")

    if not re.search(r"[A-Z]", password):
        print("its better for you to Consider using Uppercase characters in password(you lost 10/100 of your security!)")
    else:
        security_amount += 10

    if not re.search(r"[a-z]", password):
        print("its better for you to Consider using Lowercase characters in password(you lost 10/100 of your security!)")
    else:
        security_amount += 10
    
    if not re.search(r"\d", password):
        print("its better for you to Consider using digit characters in password(you lost 10/100 of your security!)")
    else:
        security_amount += 10

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("its better for you to Consider using !@#$%^&*(),.?\":{/}|<> in password(you lost 10/100 of your security in brute force attack)")
    else:
        security_amount += 10
    
    
    for i in range(len(password) - 2):
        if(i <len(password)):
            if password[i] == password[i + 1] == password[i + 2]:
                print("its better for you to Consider do not using repasted strings in password(you lost 10/100 of your security in brute force attack)")
                security_amount-=10
                break
    security_amount +=10

    if(security_amount <60): print("week password!")
    elif 60<security_amount<80: print("come on! you can do it better!")
    else: print("stronger than secure! XD")
         
if __name__ == '__main__':
   inputPassword = input('please enter your password:')
   if(fifty_most_common_passwords_set(inputPassword)):
       print("your password is in the middle of most common passwords for hackers!")
   else:
      is_password_strength_enough(inputPassword)
