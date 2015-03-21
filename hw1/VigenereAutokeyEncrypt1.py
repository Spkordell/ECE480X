#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell
if __name__ == "__main__":
    passphrase = raw_input('Passpharse: ').lower()
    plaintext = raw_input('plaintext: ').lower()

    key = (passphrase+plaintext)[:len(plaintext)]

    ciphertext = [None]*len(plaintext)

    for index, m in enumerate(plaintext):
        ciphertext[index] = ((ord(m)+ ord(key[index]) - 2*ord('a')) % 26)+ord('a')
    
    cipherTextString = ""
    cipherTextString = cipherTextString.join(map(chr,ciphertext))
    print "ciphertext: " + cipherTextString.upper()