#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 5:
# Name:Steven Kordell
# Date: 04/21/2015
# Mailbox number: 663

def my_pow(b,e,m):
    """ Computes b^e mod m using the square and multiply algorithm"""
    
    x = b
    n = m
    
    
    t = e.bit_length()        
    r = x
    for i in range(t-2,-1,-1):
        r = r**2 % n
        if e & (1 << i):
            r = r*x % n
    return r

if __name__ == "__main__": 
    #test a whole bunch of values   
    for i in range (0,1024):
        for j in range (0,1024):
            for k in range (1,1024):
                a = pow(i,j,k)
                b = my_pow(i,j,k)
                if a != b:
                    print str(a)+" "+str(b)+" "+str(i)+" "+str(j)+" "+str(k)                   