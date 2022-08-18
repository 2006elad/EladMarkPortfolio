alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, k):
    cypher_alpha = alphabet[-k::1] + alphabet[0:len(alphabet)-k:1]
    cypher_text = ""
    for ch in plaintext:
        cypher_text += cypher_alpha[alphabet.find(ch)]
    return cypher_text
