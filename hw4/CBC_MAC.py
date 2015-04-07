#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 4:
# Name:Steven Kordell
# Date: 04/13/2015
# Mailbox number: 663


from Crypto.Cipher import AES

BLOCK_SIZE = 32 #number of bytes in an AES Block

#append a pad of 1 followed by zeros until the message is evenly divisable by the block size
def padMessage(message):
    #print (len(message)/2)
    if ((len(message)/2) % BLOCK_SIZE):
        message += '80'
        while ((len(message)/2) % BLOCK_SIZE):
            message += '00'
    #print (len(message)/2)   
    return message

if __name__ == "__main__":    
    #plaintext = raw_input('plaintext: ')
    message = "The quick brown fox jumps over the lazy dog"
    #message = 'A'
    #message = '00000000000000000000000000000000'
    
    print padMessage(message.encode('hex'))
    