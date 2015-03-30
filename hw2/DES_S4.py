#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Steven Kordell

if __name__ == "__main__":
    print "hello"
    # coefficients = raw_input('Coefficients: ').lower()
    # coefficients = "000011"
    # ciphertext = raw_input('Ciphertext: ').lower()      
#     ciphertext = "j5a0edj2b".lower()
#     # starting_vector = raw_input('Starting Vector: ').lower()
#     starting_vector = 63  # 111111
#     vector = starting_vector
#     
#     lsfrOutput = []    
#     print "LSFR sequence:" 
#     print "{0:b}".format(vector)  
#     vector |= ((vector & 1) ^ ((vector & 2) >> 1)) << 6 
#     lsfrOutput.append(vector & 1) 
#     vector >>= 1    
#     while (vector != starting_vector):
#         print "{0:06b}".format(vector)
#         vector |= ((vector & 1) ^ ((vector & 2) >> 1)) << 6
#         lsfrOutput.append(vector & 1)
#         vector >>= 1
#     
#     plaintext = ""
#     index = 0
#     for c in ciphertext:
#         vec = 0
#         for i in range(5):
#             vec += lsfrOutput[index + i] << 4-i
#         plaintext += decChar(c, vec)
#         index += 5
# 
#     print "Output: " + plaintext

    
