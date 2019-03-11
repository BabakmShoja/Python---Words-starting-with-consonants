#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:44:32 2019

@author: babakmalekishoja
"""

def consonant_first(text):
    consonants=[]
    for token in set(text.split(" ",)):
        if token[0].lower() not in 'aeiuo':
            consonants.append(token.lower())
    print(consonants)
    return consonants
