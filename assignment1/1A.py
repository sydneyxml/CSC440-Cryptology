'''
CSC 440
HW1
1A
Ximan Liu
'''

def affine_encrypt(text, key): 
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)  
                  + ord('A')) for t in text.upper().replace(' ', '') ])

def main(): 
    # declare text and key 
    text = 'pandemic'
    key = [19, 12]   
    # call encryption function 
    affine_encrypted_text = affine_encrypt(text, key) 
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
    
if __name__ == '__main__': 
    main() 

