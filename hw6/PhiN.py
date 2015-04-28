#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 6:
# Name:Steven Kordell
# Date: 04/29/2015
# Mailbox number: 663

# Given N and phi(N), solve for p and q

import math

def intSqrt(square):
    ''' returns the integer square root of square
    if it exists, otherwise the closest
    integer smaller than the square root'''
    bits = int(math.log(square, 2) // 2)
    sqrt = 2 ** bits
    for idx in range(bits, -1, -1):
        if ((sqrt + 2 ** idx) ** 2 <= square):
            sqrt = sqrt + 2 ** idx
    return sqrt

if __name__ == "__main__":    
    N = 95108693570035270144657857241002423425941108178488256393099501537459309973338659032070137401466057288093251338945346909386662950709297073547026782605536851430009315154963250527483541499661777610571226461548017983537357340977791191782144166557488091378280662921890402461825132632264736288885016437441408031437
    phiN = 95108693570035270144657857241002423425941108178488256393099501537459309973338659032070137401466057288093251338945346909386662950709297073547026782605536831849545762403179260357125717820498921119322654216449244793611407031294391525498300469688335255546240141624625909322093238921327083984345759003847642930236

    # compute possible p's and q's
    q = (1 + N - phiN - intSqrt(((-1 - N + phiN) ** 2) - 4 * N)) / 2
    p = N / q
    
    print "p = " + str(p)
    print "q = " + str(q)       

    
    
