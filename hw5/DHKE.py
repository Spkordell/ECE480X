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
    #a 1024-bit prime number
    #p = 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137111

    #a 1023-bit prime number
    p = 89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270413618581675255342293149119973622969239858152417678164812112068247

    #p_s is 1024 bits
    p_s = 2*p + 1
    print p_s
    
    #choose g at random from group 
    g = random.randint(0,p_s)
    print g

    a = random.randint(1,2**1024)
    b = random.randint(1,2**1024)
    print a
    print b
    
    g_a = pow(g,a,p_s)
    g_b =pow(g,b,p_s)

    print g_a
    print g_b    
    
    k_A = pow(g_b,a,p_s)
    k_B = pow(g_a,b,p_s)
    
    print k_A
    print k_B
    
    if k_A == k_B:
        print "Keys are equal"
    
    key = hashlib.sha256(hex(k_A)[2:-1].decode('hex')).hexdigest()
    
    print key

    

    
    