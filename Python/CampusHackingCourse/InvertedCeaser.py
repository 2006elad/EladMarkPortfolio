alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)


def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)


def brute_force(ciphertext):
    for k in range(1, 27, 1):
        cipher_alpha = alphabet[-k::1] + alphabet[0:len(alphabet) - k:1]
        decipher_text = ""
        for ch in ciphertext:
            decipher_text += alphabet[cipher_alpha.find(ch)]
        print(decipher_text)


brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
