#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Project 4:
# Name:Steven Kordell
# Date: 04/13/2015
# Mailbox number: 663

import hashlib

if __name__ == "__main__":    
    
    with open('Project2.pdf','rb') as in_file:
        filehash = hashlib.sha256(in_file.read()).hexdigest()
    
        print filehash
