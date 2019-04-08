#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:59:13 2019

@author: admin
"""

class Biometric:
    """
    A Biometric for a specific actuator.
    Used for keyboard and mouse movement dynamics.
    
    """
    def __init__(self, metrics):
        self.metrics = metrics
        
    def __repr__(self):
        return 'Metrics: ' + ', '.join(self.metrics)