from datetime import datetime
from cryptography.fernet import Fernet
import os

with open('spy.key', 'rb') as key_file:
    key = key_file.read()
fernet_key = Fernet(key)

files = os.listdir("/Users/user/Documents/JustCode/FileProject2/spy_reports")
for i in range(31):
    my_date = datetime(2023, 10, i+1)
    formatted_date = my_date.strftime("%d_%m_%Y")
    flag = False
    for file in files:
        if formatted_date in file:
            flag = True
            break

    if flag:
        with open(f'spy_reports/{file}', 'rb') as f:
            encrypted_data = f.read()
        # Дешифровка данных
        decrypted_data = fernet_key.decrypt(encrypted_data)
        
        with open(f'decrypted_reports/{file}', 'wb') as decryp_f:
            decryp_f.write(decrypted_data)
    else:
        print(f"Файл не найден на дату {formatted_date}")    


