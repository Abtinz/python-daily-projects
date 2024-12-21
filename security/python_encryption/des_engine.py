import argparse

from Crypto.Cipher import DES


available_mode = ['encryption', 'decryption']


def encryption_engine(key):

    with open('plaintext.txt', 'rb') as file:
        plaintext = file.read()
   
    encoded_key = key.encode('utf-8')[:8]#keys have 8 byte space in DES

    #padding is needed for 8 byte des key(needed length is about 8 - (len(plaintext) % 8))
    plaintext += b' ' * (8 - (len(plaintext) % 8))
    cipher_box = DES.new(encoded_key, DES.MODE_ECB)
    cipher_text = cipher_box.encrypt(plaintext)
    print(cipher_text)
    #cipher text saving
    with open('encrypted_text.txt', 'wb') as file2:
        file2.write(cipher_text)

    print("text is ciphered completely")


def decryption_engine(key):

    with open('encrypted_text.txt', 'rb') as file:
        cipher_text = file.read()

    encoded_key = key.encode('utf-8')[:8]
    cipher = DES.new(encoded_key, DES.MODE_ECB)
    plaintext = cipher.decrypt(cipher_text)

    #plain text saving
    with open('decrypted_text.txt', 'wb') as file2:
        file2.write(plaintext)

    print("text is deciphered completely")

    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='DES Engine 2000.Turbo!')
    parser.add_argument('--mode', type=str, choices=available_mode,help='encryption or decryption')
    parser.add_argument('--key', type=str, help='Encryption and Decryption key')
    args = parser.parse_args()
    if args.mode == 'encryption':
        encryption_engine(args.key)
    else:
        decryption_engine(args.key)