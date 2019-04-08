#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:58:50 2019

@author: admin
"""

class Recognizer:
    """
    Used to recognize and test a user.
    """
    def __init__(self, biometrics):
        self.biometrics = biometrics
    
    def train(self, trainX, trainY):
        pass
    
    def predict(self, testX):
        pass
    
    def test(self, testX, testY):
        pass
    
    def analysis(self):
        pass