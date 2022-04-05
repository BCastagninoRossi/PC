#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:19:06 2022

@author: brunocr
"""
from game import game
from mod import mod
from p1 import p1
from p2 import p2

def main():
    print(' %%% VIRTUA TENNIS GAMMA %%% ' )
    game(mod(), p1(), p2(), 0, 0)
if __name__=='__main__':
    main()
              