#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell

from Crypto.Cipher import DES
import timeit

if __name__ == "__main__":    
    
    plaintext = '48656c6c6f212121'
    ciphertext = '1f6339383e8da6c4'
            
    encoded_ciphertext = ciphertext.encode('hex')
    start = timeit.default_timer()
    
    k = '0000000000000000'   
    ct = ''
    pt = plaintext.encode('hex')
    while ct != ciphertext and ct != encoded_ciphertext:
        key = k.decode('hex')
        a = DES.new(key)
        ct = a.encrypt(pt)   
        print '{:016X}'.format(int(k, 16)) + ': ' + ct
        
        #increment to next hex value'
        k = '{:016X}'.format(int(k, 16)+1)
               
    stop = timeit.default_timer()        
    print "key is: " + '{:016X}'.format(int(k, 16)-1)    
    print "Elapsed time: " + str(stop - start)
    
