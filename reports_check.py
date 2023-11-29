import os

files = os.listdir("/Users/user/Documents/JustCode/FileProject2/decrypted_reports")

str = 'вра'
repl = 'дру'
last_text = "Проверено!"

for f in files:
    with open(f'decrypted_reports/{f}', 'rb') as file:
        data = file.read()
        decoded_text = data.decode('utf-8')
        print(f"{f} : {decoded_text}")
        new_text = decoded_text.lower().replace(str, repl)
        # print(new_text)
    with open(f'verified/{f}', 'wb') as file:
        file.write(new_text.encode('utf-8'))  
        file.write(last_text.encode('utf-8'))

