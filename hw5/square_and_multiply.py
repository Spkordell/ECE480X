#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 5:
# Name:Steven Kordell
# Date: 04/21/2015
# Mailbox number: 663

def my_pow(b,e,m):
    """ Computes b^e mod m using the square and multiply algorithm"""
    
    #special case for things raised to the zeroth or first power
    if e == 0:
        return 1 % m
    if e == 1:
        return b % m
        
    #the square and multiply alorithm
    t = e.bit_length()        
    r = b
    for i in range(t-2,-1,-1):
        r = r**2 % m
        if e & (1 << i):
            r = r*b % m
    return r

if __name__ == "__main__":    
    print my_pow(235973,456789,583903)
    print my_pow(984327457683,2153489582,994348472629)
    
    #test a whole bunch of values      
    """
    for i in range (0,1024):
        for j in range (0,1024):
            for k in range (1,1024):
                a = pow(i,j,k)
                b = my_pow(i,j,k)
                if a != b:
                    print str(a)+" "+str(b)+" "+str(i)+" "+str(j)+" "+str(k)                 
    """       
                    
    