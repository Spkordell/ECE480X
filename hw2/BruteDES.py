#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell

from Crypto.Cipher import DES

if __name__ == "__main__":
    k = '0000000012345678'
    key = k.decode('hex')

    message = "Hello!!!"  
    m = message.encode('hex')

    a = DES.new(key)
    ct = a.encrypt(m)
    
    print ct