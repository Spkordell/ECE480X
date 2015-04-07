#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 4:
# Name:Steven Kordell
# Date: 04/06/2015
# Mailbox number: 663

import hashlib

if __name__ == "__main__":    
    
    
    with open('Gompei.bmp','rb') as in_file:
        filehash = hashlib.sha256(in_file.read()).hexdigest()
    
        print filehash
