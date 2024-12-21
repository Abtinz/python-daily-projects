import argparse
import itertools
import time
import string


search_modes = ['standard', 'first_character', 'this_known_k_latter']
search_space = ['number', 'number_lowercase', 'lowercase', 'full_space']
Success_message = "password was cracked successfully"
Failure_message = "password was not cracked at last, you are now safe from our brute force attacks!"


class InputtedArguments():

    def __init__(self, password, mode, space, password_length, first_character, k_char):
       self.password = password
       self.search_mode = mode
       self.search_space = space
       self.password_length = password_length
       self.first_character = first_character
       self.k_char = k_char

def final_search_space(chosen_space):
    match chosen_space:
        case 'number': 
            return list(string.digits)
        case 'lowercase': 
            return list(string.ascii_lowercase)
        case 'number_lowercase': 
            list(string.digits) + list(string.ascii_lowercase)
    
    return list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.punctuation)
        
def standard_mode(inputted_arguments:InputtedArguments,staring_time):

    total_attempts = 0
    search_space_list = final_search_space(chosen_space= inputted_arguments.search_space)
    
    for combination in list(itertools.product(search_space_list, repeat=inputted_arguments.password_length)):
        total_attempts += 1
        if ''.join(combination) == inputted_arguments.password:
                print(Success_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                total_attempts = 0
                break

    if total_attempts: print(Failure_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")

def first_character_mode(inputted_arguments:InputtedArguments,staring_time):

    total_attempts = 0
    search_space_list = final_search_space(chosen_space= inputted_arguments.search_space)

    if  not inputted_arguments.password_length is None:
            
            if inputted_arguments.password_length == 1: #take it easy, its just about one simple char!
               
                if inputted_arguments.first_character == inputted_arguments.password:
                    print(Success_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                else:  
                    print(Failure_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
            
            else: #a least, we have password length, its better than next state branch
                for combination in list(itertools.product(search_space_list, repeat= inputted_arguments.password_length - 1)):
                    total_attempts += 1
                    print(inputted_arguments.first_character + ''.join(combination),end = "-")
                    if inputted_arguments.first_character + ''.join(combination) == inputted_arguments.password:
                        print(Success_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                        total_attempts = 0
                        break
                if total_attempts: 
                    print(Failure_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
            
    else:
            total_attempts += 1
            if inputted_arguments.first_character == inputted_arguments.password:
                    print(Success_message + f"\n    -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
            current_length = 2
            while current_length:# welcome to disaster!
                if current_length > 10 :
                        print(Failure_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                        break
                for combination in list(itertools.product(search_space_list, repeat=current_length)):
                    total_attempts += 1
                    if inputted_arguments.first_character + ''.join(combination) == inputted_arguments.password:
                        print(Success_message + f"\n    -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                        total_attempts = 0
                        break
                if total_attempts:
                     current_length += 1
                else:
                     break

            

def k_char_mode(inputted_arguments:InputtedArguments,staring_time):
    total_attempts = 0
    search_space_list = final_search_space(chosen_space= inputted_arguments.search_space)
   
    if inputted_arguments.password_length is None:
            current_length = len(inputted_arguments.k_char)
            
            while True:
                if current_length > 10 :
                    print(Failure_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                    break
                itsFounded = False  

                for combination in list(itertools.product(search_space_list, repeat=current_length - len(inputted_arguments.k_char))):
                    current_space = list(''.join(combination)) + inputted_arguments.k_char
                    for permutation in list(itertools.permutations(current_space, current_length)):
                        total_attempts += 1
                        if ''.join(permutation) == inputted_arguments.password:
                           print(Success_message + f"\n    -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                           itsFounded = True
                           break
                    if itsFounded: break 
                if itsFounded: break 
                current_length += 1
    else:
            
            if inputted_arguments.password_length == len(inputted_arguments.k_char):
                for permutation in list(itertools.permutations(inputted_arguments.k_char, len(inputted_arguments.k_char))):
                    total_attempts += 1
                    if ''.join(permutation) == ''.join(permutation).password:
                        print(Success_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                        break
                print(Failure_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
            else:
                for combination in list(itertools.product(search_space_list, repeat=inputted_arguments.password_length - len(inputted_arguments.k_char))):
                    current_space = list(''.join(combination)) + inputted_arguments.k_char
                    for permutation in list(itertools.permutations(current_space, inputted_arguments.password_length)):
                        total_attempts += 1
                        if ''.join(permutation) == inputted_arguments.password:
                            print(Success_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
                            break
                print(Failure_message + f"\n   -total attempts{total_attempts}\n    -total time:{time.time() - staring_time}")
       
def cracker_engine(inputted_arguments:InputtedArguments):
    if  inputted_arguments.password_length is None and inputted_arguments.first_character is None and inputted_arguments.k_char is None :
          print("error! length and first_character and k_char are None at the same time!")
    else:

        #initializing starting time
        staring_time = time.time()

        if not inputted_arguments.password_length is None and inputted_arguments.search_mode == "standard":
            #searching mode is standard
            standard_mode(inputted_arguments,staring_time)

        elif not inputted_arguments.k_char is None:
            #searching mode is  k_char
            k_char_mode(inputted_arguments=inputted_arguments,staring_time=staring_time)

        elif not inputted_arguments.first_character is None:
            #searching mode is  first_character
            first_character_mode(inputted_arguments=inputted_arguments,staring_time=staring_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Password Cracker v.2000.turbo!')

    parser.add_argument('--password', type=str, help='we can\'t crack your null password! oh wait a moment: your pass == null? XD')
    parser.add_argument('--mode', type=str, choices=search_modes, help='Select your searching mode')
    parser.add_argument('--space', type=str, choices=search_space,help='Select the searching space')

    parser.add_argument('--length', type=str, nargs='?', help='length of the password is needed for cracking!')
    parser.add_argument('--first_character', type=str, nargs='?', help='If you have chosen (this_known_k_latter) mode, you must type first character of password letters')
    parser.add_argument('--k_char', type=str, nargs='+', help='If you have chosen (this_known_k_latter) mode, you must type k number of password letters')
   
    args = parser.parse_args()

    length = None
    if not args.length is None: length = int(args.length)
    cracker_engine(
        inputted_arguments= InputtedArguments(
            password= args.password, 
            mode=args.mode, 
            space=args.space,
            password_length=length , 
            first_character=args.first_character, 
            k_char=args.k_char
        )
    )
    