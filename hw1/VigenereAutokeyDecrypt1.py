#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell
if __name__ == "__main__":
    passphrase = raw_input('Passpharse: ').lower()
    ciphertext = raw_input('Ciphertext: ').lower()
    
    key = passphrase
    plaintext = [None]*len(ciphertext)
       
    for index, c in enumerate(ciphertext):
        plaintext[index] = (((ord(c) - ord('a')) - (ord(key[index]) - ord('a'))) % 26) + ord('a')
        key+=chr(plaintext[index])
        
    plainTextString = ""
    plainTextString = plainTextString.join(map(chr,plaintext))
    print "Plaintext: " + plainTextString.lower()
    