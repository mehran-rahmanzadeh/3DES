from .des import des_encrypt, des_decrypt

def encrypt(plaintext, key1, key2, key3, padding=True):
    if padding:
        pad_length = 8 - (len(plaintext) % 8)
        plaintext += bytes([pad_length] * pad_length)
    
    output = b''
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        inter1 = des_encrypt(block, key1)
        inter2 = des_decrypt(inter1, key2)
        ciphertext = des_encrypt(inter2, key3)
        output += ciphertext
    
    return output

def decrypt(ciphertext, key1, key2, key3, padding=True):
    output = b''
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
        inter1 = des_decrypt(block, key3)
        inter2 = des_encrypt(inter1, key2)
        plaintext = des_decrypt(inter2, key1)
        output += plaintext
    
    if padding:
        pad_length = output[-1]
        output = output[:-pad_length]
    
    return output

