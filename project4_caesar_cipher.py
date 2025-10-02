alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(plain_text, key): #hello h = index(k)+key % 26
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            index = alphabets.index(char)
            new_char = alphabets[(index + key) % 26]
            cipher_text += new_char
        else :
            cipher_text += char
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            index = alphabets.index(char)
            new_char = alphabets[(index - key + 26) % 26]
            plain_text += new_char
        else :
            plain_text += char
    return plain_text

flag = "yes"

while flag == "yes":
    user_input = input("Type 'encrypt' for encryption, type 'decrypt' for decryption :")
    text = input("Type your message :")
    shift_key = int(input("Type the shift key :"))
    if user_input == 'encrypt':
        encrypted_string = encrypt(text, shift_key)
        print(f"Here's the encrypted result :{encrypted_string}")
    else:
        decrypted_string = decrypt(text, shift_key)
        print(f"Here's the decrypted result :{decrypted_string}")
    flag = input("Do you want to continue? (yes/no) : ")
