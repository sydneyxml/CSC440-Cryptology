'''
CSC 440
aesencryptround.py
Ximan Liu
'''

class AES:

    MIX_C  = [[0x2, 0x3, 0x1, 0x1], [0x1, 0x2, 0x3, 0x1], [0x1, 0x1, 0x2, 0x3], [0x3, 0x1, 0x1, 0x2]]
    RCon   = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000, 0x20000000, 0x40000000, 0x80000000, 0x1B000000, 0x36000000]
    S_BOX = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
             [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
             [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
             [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
             [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
             [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
             [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
             [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
             [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
             [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
             [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
             [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
             [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
             [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
             [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
             [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]

    def SubBytes(self, State):
        return [self.S_BOX[i][j] for i, j in
               [(_ >> 4, _ & 0xF) for _ in State]]


    def ShiftRows(self, S):
        return [S[ 0], S[ 5], S[10], S[15],
                S[ 4], S[ 9], S[14], S[ 3],
                S[ 8], S[13], S[ 2], S[ 7],
                S[12], S[ 1], S[ 6], S[11]]

    def MixColumns(self, State):
        return self.Matrix_Mul(self.MIX_C, State)

    def RotWord(self, _4byte_block):
        return ((_4byte_block & 0xffffff) << 8) + (_4byte_block >> 24)

    def SubWord(self, _4byte_block):
        result = 0
        for position in range(4):
            i = _4byte_block >> position * 8 + 4 & 0xf
            j = _4byte_block >> position * 8 & 0xf
            result ^= self.S_BOX[i][j] << position * 8
        return result

    def mod(self, poly, mod = 0b100011011):
        while poly.bit_length() > 8:
            poly ^= mod << poly.bit_length() - 9
        return poly

    def mul(self, poly1, poly2):
        result = 0
        for index in range(poly2.bit_length()):
            if poly2 & 1 << index:
                result ^= poly1 << index
        return result

    def Matrix_Mul(self, M1, M2):
        M = [0] * 16
        for row in range(4):
            for col in range(4):
                for Round in range(4):
                    M[row + col*4] ^= self.mul(M1[row][Round], M2[Round+col*4])
                M[row + col*4] = self.mod(M[row + col*4])
        return M

    def round_key_generator(self, _16bytes_key):
        w = [_16bytes_key >> 96,
             _16bytes_key >> 64 & 0xFFFFFFFF,
             _16bytes_key >> 32 & 0xFFFFFFFF,
             _16bytes_key & 0xFFFFFFFF] + [0]*40
        for i in range(4, 44):
            temp = w[i - 1]
            if not i % 4:
                temp = self.SubWord(self.RotWord(temp)) ^ self.RCon[i//4-1]
            w[i] = w[i-4] ^ temp
        return [self.num_2_16bytes(
                    sum([w[4 * i] << 96, w[4*i+1] << 64,
                         w[4*i+2] << 32, w[4*i+3]])
                    ) for i in range(11)]

    def AddRoundKey(self, State, RoundKeys, index):
        return self._16bytes_xor(State, RoundKeys[index])

    def _16bytes_xor(self, _16bytes_1, _16bytes_2):
        return [_16bytes_1[i] ^ _16bytes_2[i] for i in range(16)]

    def _16bytes2num(cls, _16bytes):
        return int.from_bytes(_16bytes, byteorder = 'big')

    def num_2_16bytes(cls, num):
        return num.to_bytes(16, byteorder = 'big')

    def aes_encrypt1round(self, plaintext_list, RoundKeys):
        State = plaintext_list

        s1_1 = [hex(item) for item in State]
        s1_2 = [remove_punc(item) for item in s1_1]
        s1_3 = [s1_2[i * 4:(i + 1) * 4] for i in range((len(s1_2) + 4 - 1) // 4 )]  
        print("Original plaintext")
        table(s1_3)
        print()

        State = self.AddRoundKey(State, RoundKeys, 0)
        s2_1 = [hex(item) for item in State]
        s2_2 = [remove_punc(item) for item in s2_1]
        s2_3 = [s2_2[i * 4:(i + 1) * 4] for i in range((len(s2_2) + 4 - 1) // 4 )] 
        print("After ARK with original key")
        table(s2_3)
        print()

        State = self.SubBytes(State)
        s3_1 = [hex(item) for item in State]
        s3_2 = [remove_punc(item) for item in s3_1]
        s3_3 = [s3_2[i * 4:(i + 1) * 4] for i in range((len(s3_2) + 4 - 1) // 4 )] 
        print("After SB")
        table(s3_3)
        print()

        State = self.ShiftRows(State)
        s4_1 = [hex(item) for item in State]
        s4_2 = [remove_punc(item) for item in s4_1]
        s4_3 = [s4_2[i * 4:(i + 1) * 4] for i in range((len(s4_2) + 4 - 1) // 4 )] 
        print("After SR")
        table(s4_3)
        print()

        State = self.MixColumns(State)
        s5_1 = [hex(item) for item in State]
        s5_2 = [remove_punc(item) for item in s5_1]
        s5_3 = [s5_2[i * 4:(i + 1) * 4] for i in range((len(s5_2) + 4 - 1) // 4 )] 
        print("After MC")
        table(s5_3)
        print()

        return State

def remove_punc(string):
    if len(string) == 3:
        string = string[0:2] + '0' + string[2:]        
    string = string[2:]
    if len(string) == 1:
        string = string + '0'
    return string


def table(lst):
    count = 0
    for y in range(len(lst[0])):
        for x in range(len(lst)):
            print(lst[x][y], end=' ')
            count += 1
            if count % 4 == 0:
                print(end='\n')            
    print()
 

aes = AES()
key = 0x2b7e151628aed2a6abf7158809cf4f3c
RoundKeys = aes.round_key_generator(key)
plaintext = 0x3243f6a8885a308d313198a2e0370734
plaintext = aes.num_2_16bytes(plaintext)
ciphertext = aes.aes_encrypt1round(plaintext, RoundKeys)

