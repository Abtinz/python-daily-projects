import itertools
import random
import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def padding_function(text):
    padding = AES.block_size - (len(text) % AES.block_size)
    return text + bytes([padding] * padding)

def encrypt(password, plaintext):

    # generating a random key length (128, 192, or 256 bits) based on the password for random output len
    key_length = len(password) % 3
    key_length_options = [128, 192, 256]
    key_length = key_length_options[key_length]
    key = get_random_bytes(key_length // 8)
    
    cipher = AES.new(key, AES.MODE_ECB)

    padded_text = padding_function(plaintext.encode('utf-8'))
    ciphered_text = cipher.encrypt(padded_text)
    encrypted_text = base64.b64encode(ciphered_text).decode()

    return encrypted_text

def generate_combinations():
   
    file_name = file_name_entry.get()
    password = password_label.get()

    if not file_name:
        messagebox.showerror("Missing File Name", "Please enter a file name.")
        return

    characters = [chr(i) for i in range(48, 58)]  # Numbers 0-9
    characters += [chr(i) for i in range(65, 91)]  # Uppercase letters A-Z
    characters += [chr(i) for i in range(97, 123)]  # Lowercase letters a-z
    # Generate combinations within the specified string length range
    combinations = [ ''.join(combination) for combination in itertools.product(characters, repeat=len(password))]
    print(len(combinations))

    #password encryptor is here for new passwords
    passwords = []
    for item in combinations:
        passwords.append(encrypt(password,item))

    # Save combinations to a file
    if not ".txt" in file_name:
        file_name += ".txt"
    with open(file_name, "wb") as file:
        for password in passwords[:10000]:
            file.write(str(password) + "\n")

    messagebox.showinfo("Combinations Generated", f"The combinations have been saved to {file_name}.")

window = tk.Tk()
window.title("Combination Generator turbo charge made in aut")
window.geometry("300x200")

window.configure(bg="#2196f3")
label_bg = "#2196f3"
button_bg = "#1976d2"
button_fg = "white"

password_label = tk.Label(window, text="password:", bg=label_bg)
password_label.pack()
password_label = tk.Entry(window)
password_label.pack()

file_name_label = tk.Label(window, text="File Name:", bg=label_bg)
file_name_label.pack()
file_name_entry = tk.Entry(window)
file_name_entry.pack()

generate_button = tk.Button(window, text="Generate Combinations", command=generate_combinations, bg=button_bg, fg=button_fg)
generate_button.pack()

window.mainloop()