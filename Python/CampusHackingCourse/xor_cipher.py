import math


def encrypt(plaintext, key):
    plaintext_binary_list = to_binary(plaintext)
    key_binary_list = to_binary(key)
    ciphered_chr_list = []
    for pbl, kbl in zip(plaintext_binary_list, key_binary_list):
        cbl = []
        sum_bin = 0
        for one_pb, one_kb in zip(pbl, kbl):
            cbl.append(str(int(one_pb) ^ int(one_kb)))
        pow_count = 7
        for one_bin in cbl:
            sum_bin += int(one_bin) * pow(2, pow_count)
            pow_count -= 1
        ciphered_chr_list.append(chr(sum_bin))
    return "".join(ciphered_chr_list)


def to_binary(a):
    ord_list, bin_list = [], []
    for ch in a:
        ord_list.append(ord(ch))
    for one_ch_ord in ord_list:
        bin_list.append((bin(one_ch_ord))[2:].zfill(8))
    return bin_list


ciphered_text = encrypt("ab", "cd")
print(ciphered_text)
