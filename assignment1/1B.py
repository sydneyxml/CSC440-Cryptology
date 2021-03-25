'''
CSC 440
HW1
1B
Ximan Liu
'''

# Extend euclidean algorithm for finding mod inverse
def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 

def modinv(a, m): 
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None
    else: 
        return x % m 


# affine cipher decryption function  
# return original text 
def affine_decrypt(cipher, key): 
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))  
                    % 26) + ord('A')) for c in cipher ]) 
  
  
# main 
def main(): 
    # declare text and key 
    affine_encrypted_text = 'LMZRKGIY'
    key = [19, 12] 
  
    # call decryption function 
    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine_encrypted_text, key) )) 
  
  
if __name__ == '__main__': 
    main() 

