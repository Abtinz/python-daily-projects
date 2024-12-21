import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import tkinter as tk
from tkinter import messagebox

#this function will add padding for our 16 byte AES 
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

#saving the new password to the specific filename with given name
def save_to_file(filename, encrypted_password, name, description):
    with open(filename, 'w') as file:
        file.write(f"Encrypted Password: {encrypted_password}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Description: {description}\n")

#saving the and encrypting given password
def encrypt_and_save():
    password = password_entry.get()
    name = name_entry.get()
    description = description_entry.get()

    if password and name and description:
        try:
            encrypted_password = encrypt(password, password)

            # Save the encrypted password, name, and description to a text file
            filename = name + "_encrypted_password.txt"
            save_to_file(filename, encrypted_password, name, description)
            messagebox.showinfo("Password generation is Completed", f"The password has been encrypted and saved successfully in this route {filename}")

        except Exception as error:
            messagebox.showerror("Error", f"An error occurred during encryption: {str(error)}")

    else:
        messagebox.showwarning("Missing Information ...", "Please fill in all the fields.")

#this function will remove given name password from os ...
def remove_password():

    name = name_entry.get()

    if name:
        try:
            filename = name + "_encrypted_password.txt"
            os.remove(filename)

            messagebox.showinfo("Password Removed", "The password has been removed successfully.")
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "The encrypted data file was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while removing the password: {str(e)}")
    else:
        messagebox.showwarning("Missing Information!!!", "Please enter the name of the password to remove...")

# Creating the main window for inputs demonstration and colors
window = tk.Tk()
window.title("Password Encryptor(Turbo 2000.v1 fast charge XD)")
window.geometry("500x200")

#colors
window.configure(bg="#2196f3")
label_bg = "#2196f3"
button_bg = "#1976d2"
button_fg = "white"

#inputs
password_label = tk.Label(window, text="Password:", bg=label_bg)
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

name_label = tk.Label(window, text="Name:", bg=label_bg)
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

description_label = tk.Label(window, text="Description:", bg=label_bg)
description_label.pack()
description_entry = tk.Entry(window)
description_entry.pack()

#buttons section
encrypt_button = tk.Button(window, text="Encrypt and Save", command=encrypt_and_save, bg=button_bg, fg=button_fg)
encrypt_button.pack()

remove_button = tk.Button(window, text="Remove Password", command=remove_password, bg=button_bg, fg=button_fg)
remove_button.pack()

window.mainloop()