def encrypt(plaintext, key):
    ciphered_chr_list = []
    for chpbl, chkbl in zip(plaintext, key):
        ciphered_chr_list.append(chr(ord(chpbl) ^ ord(chkbl)))
    return "".join(ciphered_chr_list)


ciphered_text = encrypt("ab", "cd")
print(ciphered_text)