'''
CSC 440
HW4
Ximan Liu
'''

def encryptRound(plaintext, subkey):
    pt = "{0:012b}".format(plaintext)
    sk = "{0:09b}".format(subkey)

    l0 = pt[0 : 6]
    r0 = pt[6 : ]
    
    k1 = sk [0 : 8]
    
    E_r0 = r0[0 : 2] + r0[3] + r0[2] + r0[3] + r0[2] + r0[4 : ]

    total = "{0:08b}".format(int(E_r0, 2) ^ int(k1, 2))

    s1_input = (str(total))[0 : 4]
    s2_input = (str(total))[4 : 8]

    s1_1 = ["101", "010", "001", "110", "011", "100", "111", "000"]
    s1_2 = ["001", "100", "110", "010", "000", "111", "101", "011"]

    s2_1 = ["100", "000", "110", "101", "111", "001", "011", "010"]
    s2_2 = ["101", "011", "000", "111", "110", "010", "001", "100"]


    f_r0_k1 = ""
    if (s1_input[0] == 0):
        result_s1 = s1_1[int(s1_input[1:4], 2)]
        f_r0_k1 += result_s1
    else:
        result_s1 = s1_2[int(s1_input[1:4], 2)]
        f_r0_k1 += result_s1

  
    if (s2_input[0] == 0):
        result_s2 = s2_1[int(s2_input[1:4], 2)]
        f_r0_k1 += result_s2
    else:
        result_s2 = s2_2[int(s2_input[1:4], 2)]
        f_r0_k1 += result_s2
        
    l1 = r0
    r1 = "{0:06b}".format(int(l0, 2) ^ int(f_r0_k1, 2))
    
    result = int((l1 + str(r1)), 2)
    print("Ciphertext: ", result)


def main():
    plaintext = int(input("Enter plaintext here:"))
    subkey = int(input("Enter subkey here:"))
    encryptRound(plaintext, subkey)

if __name__ == "__main__":
    main()

    
    
    
    
    
