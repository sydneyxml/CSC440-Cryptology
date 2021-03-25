'''
CSC 440
HW2
1
Ximan Liu
'''

def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1


a = 34
m = 35

print(modInverse(a, m))

