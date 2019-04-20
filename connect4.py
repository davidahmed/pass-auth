#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:42:47 2019

@author: Sire Abe
"""

import os

board = []

def create_board(rows, columns):
    # build a single row
    columns = []
    for each in columns:
        columns.append(' ')
    
    # build a board with n rows
    for each in range(rows):
        board.append(columns)
        
        
def show_board():
    for row in board:
        for cell in row:
            print(cell, end='|')
        print()
        
create_board(4,4)
show_board()