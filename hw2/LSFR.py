#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell


def ntoa(x):
    return {
        '0': 26,
        '1': 27,
        '2': 28,
        '3': 29,
        '4': 30,
        '5': 31,
    }[x]

def decChar(char, vector):
    num = ord(char)-ord('a')
    bin = 0
    if (num < 0):
        num = ntoa(char)
    index = 0;
    for c in vector:
        if c == '1':
            bin += 2**index
    res = bin ^ num
    if (res > 25):
        return aton(res)
    else:
        return chr(res+ord('a'))

if __name__ == "__main__":
    #coefficients = raw_input('Coefficients: ').lower()
    #coefficients = "000011"
    #ciphertext = raw_input('Ciphertext: ').lower()      
    ciphertext = "j5a0edj2b".lower()
    #starting_vector = raw_input('Starting Vector: ').lower()
    starting_vector = 31#111111
    vector = starting_vector
    
    plaintext = ""
    
    print "LSFR sequence:" 
    print vector
    #plaintext = plaintext+decChar(ciphertext[0],vector)
    vector = str(int(vector[4]) ^ int(vector[5])) + vector[:-1]   
    index = 4
    while (vector != starting_vector):
        print vector
        if (index % 5 == 0):
            #plaintext = plaintext+decChar(ciphertext[0],vector[:-5])
            print "h"
        vector = str(int(vector[4]) ^ int(vector[5])) + vector[:-1]
        index+=1
    
    print plaintext
        
#     key = passphrase
#     plaintext = [None]*len(ciphertext)
#        
#     for index, c in enumerate(ciphertext):
#         plaintext[index] = (((ord(c) - ord('a')) - (ord(key[index]) - ord('a'))) % 26) + ord('a')
#         key+=chr(plaintext[index])
#         
#     plainTextString = ""
#     plainTextString = plainTextString.join(map(chr,plaintext))
#     print "Plaintext: " + plainTextString.lower()
    