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

def aton(x):
    return {
         26:'0',
         27:'1',
         28:'2',
         29:'3',
         30:'4',
         31:'5',
    }[x]

def decChar(char, vector):
    num = ord(char) - ord('a')
    if (num < 0):
        num = ntoa(char)
    res = num ^ vector
    if (res > 25):
        return aton(res)
    else:
        return chr(res+ord('a'))

if __name__ == "__main__":
    # coefficients = raw_input('Coefficients: ').lower()
    # coefficients = "000011"
    # ciphertext = raw_input('Ciphertext: ').lower()      
    ciphertext = "j5a0edj2b".lower()
    # starting_vector = raw_input('Starting Vector: ').lower()
    starting_vector = 63  # 111111
    vector = starting_vector
    
    lsfrOutput = []    
    print "LSFR sequence:" 
    print "{0:b}".format(vector)  
    vector |= ((vector & 1) ^ ((vector & 2) >> 1)) << 6 
    lsfrOutput.append(vector & 1) 
    vector >>= 1    
    while (vector != starting_vector):
        print "{0:06b}".format(vector)
        vector |= ((vector & 1) ^ ((vector & 2) >> 1)) << 6
        lsfrOutput.append(vector & 1)
        vector >>= 1
    
    plaintext = ""
    index = 0
    for c in ciphertext:
        vec = 0
        for i in range(5):
            vec += lsfrOutput[index + i] << 4-i
        plaintext += decChar(c, vec)
        index += 5

    print "Output: " + plaintext

    
