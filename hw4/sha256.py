#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 4:
# Name:Steven Kordell
# Date: 04/06/2015
# Mailbox number: 663

import hashlib

if __name__ == "__main__":    
    #plaintext = raw_input('plaintext: ')
    plaintext1 = "The quick brown fox jumps over the lazy dog"
    plaintext2 = "The quick brown fox jumps over the lazy doh"
    
    hash1 = hashlib.sha256(plaintext1).hexdigest()
    hash2 = hashlib.sha256(plaintext2).hexdigest()
    
    print plaintext1 + ": " + hash1
    print plaintext2 + ": " + hash2
    