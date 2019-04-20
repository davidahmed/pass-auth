#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:58:50 2019

@author: admin
"""

import numpy as np
from passauth import utils
from passauth import data

class Authenticator:
    def __init__(self, path, k_params={}, m_params={'padding':200}):
        self.user_data = data.UserData(filepath=path)
        self.keystroke = self.user_data.getWrangledData('kb', **k_params)
        self.mouse_data = self.user_data.getWrangledData('mouse', **m_params)
        
    def __str__(self):
        return str(len(self.keystroke))
    

            
    def get_keystroke_data(self, data, method=0, normalize=False):
        self.username = []
        self.password = []
        self.combined = []
        self.k_y = []

        for each in data:
            self.username.append(bin((each[0])))
            self.password.append(bin((each[1])))
            self.combined.append(bin((each[0] + each[1])))
            self.k_y.append(each[2])
    
        if method == 0:
            return np.array(self.username), np.array(self.k_y)
        elif method == 1:
            return np.array(self.password), np.array(self.k_y)
        else:
            return np.array(self.combined), np.array(self.k_y)

        
    def get_mouse_data(self, data, method=0):
        dataX = []
        dataY = []
        
        if method == 0: # train using the 3*padding vector
            for each in data:
                dataX.append(each[0])
                dataY.append(each[1])
            padding = 3
        elif method == 1: # train using the 2*padding vector
        
            for each in data:
                dataX.append(list(map(utils.logify, each[0])))
                dataY.append(each[1])
            padding = 2
            
        dataX = np.array(dataX)
        dataX = dataX.reshape(len(dataX), len(dataX[0])*padding)    
        dataY = np.array(dataY)
        dataY = dataY.reshape(len(data),)
            
        return dataX, dataY

    
    def train_test(self, metric=None):
        for each in metric:
            dataX = None
            dataY = None
            
            if each == 'mouse':
                dataX, dataY = self.get_mouse_data(self.mouse_data)
                self.train_test_mouse(dataX, dataY)
            
            elif each == 'keystroke':
                dataX, dataY = self.get_keystroke_data(self.keystroke_data)

