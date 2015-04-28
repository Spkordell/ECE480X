#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 6:
# Name:Steven Kordell
# Date: 04/29/2015
# Mailbox number: 663

from random import randint
from fractions import gcd

magN = 1024
magM = 256
padlength = magN - magM - 1

def egcd(a, b):
    #extended eucleadian algorithm for finding inverses
    #source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    #source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def keygen():
    from Crypto.PublicKey import RSA
    #choose two large primes p, q
    genPrime = RSA.generate(1024)
    p = getattr(genPrime.key, 'p')
    q = getattr(genPrime.key, 'q')
    #compute N = p*q
    N = p*q
    #compute phiN = (p-1)(q-1)
    phiN = (p-1)*(q-1)
    # choose e such that gcd(e,phiN) =1
    e = (2**16)+1 #use a standared value for e
    #conpute d = e^-1 mod phiN
    d = modinv(e,phiN)    
    #retrun public and private keys
    k_pub = [N,e]
    k_sec = [N,d]
    return [k_pub,k_sec]

def enc(m, k_pub):    
    [N,e] = k_pub    
    r = randint(0, 2 ** padlength)
    mprime = (r << padlength) | m
    
    return pow(m,e,N)
    return pow(mprime, e, N) #ciphertext

def dec(c, k_sec):
    [N,d] = k_sec  
    mprime = pow(c,d,N)
    print mprime & ((2**magM)-1)
    return mprime & ((2**magM)-1) #plaintext
    
if __name__ == "__main__":       
    [k_pub, k_sec] = keygen() #generate random key pair
    m = randint(0,2^256-1) #generate random message to test with

    print m
    c = enc(m,k_pub)
    print c
    m1 = dec(c,k_sec)
    print m1


    if m == m1:
        print("Correct")
    else:
        print("Wrong")


