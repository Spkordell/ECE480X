#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell
if __name__ == "__main__":    
    ciphertext = raw_input('ciphertext: ').lower()
    #ciphertext = "NEASJFINVCMMZJPQKSQXIKXJBZXLXO".lower()

    for phraselength in range(1,len(ciphertext)):
        plaintext = [ord('?')]*len(ciphertext)
        for index in range(phraselength,len(ciphertext)):
            plaintext[index] = (((ord(ciphertext[index]) - ord('a')) - (ord(ciphertext[index-phraselength]) - ord('a'))) % 26) + ord('a')
        
        plainTextString = ""
        plainTextString = plainTextString.join(map(chr,plaintext))
        print "Possible Plaintext: " + plainTextString.lower()
    