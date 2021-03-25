'''
CSC 440
sdes.py
Ximan Liu
'''

import binascii
from textwrap import wrap


# encryption
def encrypt(plaintext, key):    
    plaintext = bin(plaintext)[2:]
    while (len(plaintext) < 12):
        plaintext = "0" + plaintext

    key = bin(key)[2:]
    while (len(key) < 9):
        key = "0" + key

    s1 = [["101", "010", "001", "110", "011", "100", "111", "000"],
          ["001", "100", "110", "010", "000", "111", "101", "011"]]
    s2 = [["100", "000", "110", "101", "111", "001", "011", "010"],
          ["101", "011", "000", "111", "110", "010", "001", "100"]]
    
    block = wrap(plaintext, 12)    
    block[-1] = block[-1].ljust(12, "0")[:12]    
    keys = key * 2
    subkey = [keys[0:8], keys[1:9], keys[2:10], keys[3:11]]
    
    ciphertext = ""
    
    for i in range(0, len(block)):
        cipherblock = block[i]
        left = cipherblock[:len(cipherblock)//2]
        right = cipherblock[len(cipherblock)//2:]
        for j in range (0, 4):
            l = left
            sk = subkey[j]
            left = right
            right = toAll(right)
            right = XOR(right, sk, 8)
            r1 = right[:len(right)//2]
            r2 = right[len(right)//2:]
            s1_1 = int(r1[0])
            s1_2 = int(r1[1:], 2)
            s2_1 = int(r2[0])
            s2_2 = int(r2[1:], 2)    
            sbox1 = s1[s1_1][s1_2]
            sbox2 = s2[s2_1][s2_2]
            result = sbox1 + sbox2
            right = XOR(l, result, 6)
        ciphertext += left + right
        
    if len(ciphertext) == 0:
        return 0
    else:
        ciphertext = int(ciphertext, 2)

    return ciphertext


def toAll(sb):
    toall = sb[0] + sb[1] + sb[3] + sb[2] + sb[3] + sb[2] + sb[4] + sb[5]
    return toall


def XOR(s1, s2, n):
    n1 = int(s1, 2)
    n2 = int(s2, 2)
    n3 = bin(n1 ^ n2)[2:]
    n4 = n - len(n3)
    n5 = "0" * n4
    n3 = n5 + n3
    return n3    


# decryption
def decrypt(ciphertext, key):    
    ciphertext = bin(ciphertext)[2:]
    while (len(ciphertext) < 12):
        ciphertext = "0" + ciphertext

    key = bin(key)[2:]
    while (len(key) < 9):
        key = "0" + key
    
    s1 = [["101", "010", "001", "110", "011", "100", "111", "000"],
          ["001", "100", "110", "010", "000", "111", "101", "011"]]
    s2 = [["100", "000", "110", "101", "111", "001", "011", "010"],
          ["101", "011", "000", "111", "110", "010", "001", "100"]]
    
    block = wrap(ciphertext, 12)
    block[-1] = block[-1].ljust(12, "0")[:12]
    keys = key * 2
    subkey = [keys[0:8], keys[1:9], keys[2:10], keys[3:11]]
    
    plaintext = ""
    
    for i in range(len(block) - 1, -1, -1):
        plainblock = block[i]
        left = plainblock[:len(plainblock)//2]
        right = plainblock[len(plainblock)//2:]
        for j in range(3, -1, -1):
            l = left
            r = toAll(l)
            cross = XOR(r, subkey[j], 8)
            r1 = cross[:len(cross)//2]
            r2 = cross[len(cross)//2:]
            s1_1 = int(r1[0])
            s1_2 = int(r1[1:],2)
            s2_1 = int(r2[0])
            s2_2 = int(r2[1:],2)       
            sbox1 = s1[s1_1][s1_2]
            sbox2 = s2[s2_1][s2_2]
            result = sbox1 + sbox2
            left = XOR(right, result, 6)
            right = l
        plaintext = left + right + plaintext
    
    if len(plaintext) == 0:
        return 0
    else:
        plaintext = int(plaintext, 2)

    return plaintext


# main
letter, k, way = input().split()
if letter == "e":
    # encryption
    if (k.isdigit() and way.isdigit()): 
        ct = encrypt(int(way), int(k))
        print("\nCiphertext: " + str(ct))
    else: 
        print("Invalid. ")

elif letter == "d":
    # decryption
    if (k.isdigit() and way.isdigit()): 
        pt = decrypt(int(way), int(k))
        print("\nPlaintext: " + str(pt))
    else: 
        print("Invalid. ")

else:
    print("Invalid. ")

