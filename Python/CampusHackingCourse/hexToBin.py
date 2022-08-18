cipher_text_one = \x26\x7f\x51\x95
cipher_text_two = '\x46\x06\x3e\xf3'
key_stream = '\x34\x71\x58\x94'
bin_cipher_one = "".join(format(ord(ch), 'b') for ch in cipher_text_one)
bin_cipher_two = "".join(format(ord(ch), 'b') for ch in cipher_text_two)
key_stream = "".join(format(ord(ch), 'b') for ch in key_stream)
# xor_1 = bin_cipher_one ^ key_stream
print(bin_cipher_one)
print(bin_cipher_two)
print(key_stream)
