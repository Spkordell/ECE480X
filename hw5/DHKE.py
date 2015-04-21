#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 5:
# Name:Steven Kordell
# Date: 04/21/2015
# Mailbox number: 663

#Diffie Hellman Key Exchange

import random
import hashlib

if __name__ == "__main__":    
    random.seed(12345)
    #A 1023-bit prime number (when doubled this will be 1024-bits)
    p = 89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270413618581675255342293149119973622969239858152417678164812112068247
    #p_s is A 1024 bit safe prime 
    p_s = 2*p + 1
    print p_s
    #choose g at random from group 
    g = random.randint(0,p_s)
    #choose A and B at random
    A = random.randint(1,2**1024)
    B = random.randint(1,2**1024)
    #compute powers
    g_a = pow(g,A,p_s)
    g_b =pow(g,B,p_s)
    #compute 1024 bit key
    k_A = pow(g_b,A,p_s)
    k_B = pow(g_a,B,p_s)
    #check that keys are equal
    if k_A == k_B:
        print "Keys are equal"
    else:
        print "Keys are not equal"
    #hash the key    
    key = hashlib.sha256(hex(k_A)[2:-1].decode('hex')).hexdigest()
    
    print key

    

    
    