#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell

from Crypto.Cipher import DES

if __name__ == "__main__":    
    plaintext = '48656c6c6f212121'
    ciphertext = '1f6339383e8da6c4'
            
    k = '0000000000000000'   
    ct = ''
    while ct != ciphertext:
        key = k.decode('hex')
        a = DES.new(key)
        ct = a.encrypt(plaintext.encode('hex'))   
        print '{:016X}'.format(int(k, 16)) + ' : ' + ct
       
        #increment to next hex value'
        k = '{:016X}'.format(int(k, 16)+1)
    print "key is: " + '{:016X}'.format(int(k, 16)-1)