import os
import hashlib
import random

def hash_key(key):
    return hashlib.sha256(str(key).encode('utf-8')).hexdigest()

def store_key_hash(file_name, key):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(hash_key(key))

def verify_key(file_name, key):
    with open(file_name, 'r', encoding='utf-8') as f:
        stored_key_hash = f.read()
    return hash_key(key) == stored_key_hash

def encrypt_string(input_string: str, file_name:str, key: int, keyfile: str):
    encrypted_string = ''.join(chr((ord(c) ^ key) % 256) for c in input_string)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(encrypted_string)
    store_key_hash(keyfile, key)

def decrypt_string(file_name: str, key: int, keyfile: str):
    if verify_key(keyfile, key):
        with open(file_name, "r", encoding="utf-8") as f:
            encrypted_string = f.read()
        decrypted_string = ''.join(chr((ord(c) ^ key) % 256) for c in encrypted_string)
        return decrypted_string
    else:
        raise ValueError("Invalid key or keyfile.")
    

def combine_strings(name, password, questions, answers):
    combined_string = name + "\n" + password + "\n"

    for i in range(len(questions)):
        combined_string += str(questions[i]) + "\n" + str(answers[i]) + "\n"

    return combined_string
    
name = "John Doe"
password = "my_password"
questions = ["What is your favorite color?", "What is your pet's name?"]
answers = ["Blue", "Buddy"]

result = combine_strings(name, password, questions, answers)
    

encrypt_string(result, "encrypted.txt", 12 , "keyfile.txt")

encrypt_string("result", "encrypted1.txt", 123 , "keyfile2.txt")
print(decrypt_string( "encrypted.txt", 12, "keyfile.txt"))
print(decrypt_string( "encrypted1.txt", 123, "keyfile2.txt"))

print(result==decrypt_string( "encrypted.txt", 12, "keyfile.txt"))
