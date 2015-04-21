#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 5:
# Name:Steven Kordell
# Date: 04/21/2015
# Mailbox number: 663

import fractions

if __name__ == "__main__":    
    n = 11;   
    #finds all the group elements
    count = 0
    for i in range(0,n):
        if fractions.gcd(i,n) == 1:
            print i
            count+=1
    print "numer of elemnts = " + str(count) 

    
    