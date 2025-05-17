from scripts.triple_des import encrypt, decrypt

if __name__ == '__main__':
    PADDING = True
    if PADDING:
        print("## Padding is enabled ##")
    else:
        print("## Padding is disabled ##")

    plaintext = b"Hello I'm mehran and here is my secret message"
    print('Plaintext length: ', len(plaintext))

    print("\n")

    print("## same key for 3 stages ##")
    key1 = b'0123456789ABCDEF'
    key2 = b'0123456789ABCDEF'
    key3 = b'0123456789ABCDEF'
    ct = encrypt(plaintext, key1, key2, key3, padding=PADDING)
    print('Ciphertext:', ct.hex().upper())
    pt = decrypt(ct, key1, key2, key3, padding=PADDING)
    print('Decrypted:', pt)

    print("\n")

    print("## same keys for stage 1 and 2 and different key for stage 3 ##")
    key1 = b'0123456789ABCDEF'
    key2 = b'0123456789ABCDEF'
    key3 = b'23456789ABCDEF01'
    ct = encrypt(plaintext, key1, key2, key3, padding=PADDING)
    print('Ciphertext:', ct.hex().upper())
    pt = decrypt(ct, key1, key2, key3, padding=PADDING)
    print('Decrypted:', pt)

    print("\n")

    print("## different keys for all stages ##")
    key1 = b'0123456789ABCDEF'
    key2 = b'23456789ABCDEF01'
    key3 = b'3456789ABCDEF012'
    ct = encrypt(plaintext, key1, key2, key3, padding=PADDING)
    print('Ciphertext:', ct.hex().upper())
    pt = decrypt(ct, key1, key2, key3, padding=PADDING)
    print('Decrypted:', pt)
