from cryptography.fernet import Fernet
import os

with open('spy.key', 'rb') as key_file:
    key = key_file.read()
fernet_key = Fernet(key)

files = os.listdir("/Users/user/Documents/JustCode/FileProject2/decrypted_reports")

for file in files:
    if 'c' in file:
        print("В названии папки есть буква 'c'.")
    else:
        with open(f'spy_reports/{file}', 'rb') as f:
            data = f.read()
        encrypted_data = fernet_key.encrypt(data)
        with open(f'encrypted_reports/{file}', 'wb') as encryp_f:
            encryp_f.write(encrypted_data)