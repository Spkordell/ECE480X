#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell

from numpy import array

def S4(x):
    S4 = array([
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]])

    return S4[(x & 1) | (x >> 4), (x >> 1 & 0b1111)]   

def compSAC(i):
    sum = 0   
    for i in range(5):
        sum += S4(1 << i) ^ S4((1 << i) ^ (2 ** i))
    return sum

if __name__ == "__main__":
        
    print compSAC(0)
    print compSAC(1)
    print compSAC(2)
    print compSAC(3)
    print compSAC(4)
    print compSAC(5)
