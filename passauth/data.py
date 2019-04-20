#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:08:49 2019

@author: admin
"""
import ast
import re

from os import listdir
from os.path import isfile, join

from passauth import utils


def getFields(entry:str)->dict:
    
    """
    Returns username, passHash, usernameFieldLogs and Headers from the entry
    """
    
    entry = separateFields(entry)
    return { 
        "user": entry[0].split(':')[-1].strip().replace('"', ''),
        "pass": int(entry[1].split(':')[-1]),
        "usernameFieldLogs": ast.literal_eval(entry[2].split(':')[-1].strip()),
        "passwordFieldLogs": ast.literal_eval(entry[3].split(':')[-1].strip()),
        "mouseMovements": ast.literal_eval(entry[4].split(':')[-1].strip()),
        "headers": parseHTTPHeaders(entry[5].split('":')[-1].strip()),
        "time": int(entry[6].split(":")[-1].replace('}', '').strip())
        }


def separateFields(entry:str)->list:
    
    """
    Separates the entry into 6 fields- mouseMovements, usernameLog,...headers, timestamp.
    """
    
    entry = entry.split(', "')
    res = entry[0:5]
    res.append(''.join(entry[5:-1]))
    res.append(entry[-1])
    return res


def parseHTTPHeaders(header_str:str)->dict:
    
    """
    Parse the HTTP header from the fields.
    """
    
    header_str =  re.findall(r'\("[^)]*"\)', header_str)
    header_str = [[_.replace('"', '') for _ in re.findall(r'(?=("[^"]+)")', each)[0:2]] for each in header_str]
    return dict(header_str)


    
class UserData:
    """
    Handling and maintaining all user data from the server
    
    Attributes:
        filepath (str): path to the directory storing the user data
    """
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.onlyfiles = [f for f in listdir(self.filepath) if isfile(join(self.filepath, f))]
        self.onlyfiles.remove('common_unames.txt')

    def __str__(self):
        return self.filepath + "; total users: " + str(len(self.onlyfiles))
    
    def __len__(self):
        return len(self.onlyfiles)
    
    def getUserData(self, user : int) -> [dict]:
        with open(self.filepath + self.onlyfiles[user], 'r') as f:
            content = f.read().replace("\'", '"').replace('}{', '}#{').split('#')
            return [getFields(_) for _ in content]
        
    def getWrangledData(self, type, min_entries=0, padding=None):
        data = []
        for i in range(len(self)):
            data.append(self.getUserData(i))
            
        if min_entries !=0:    
            data = list(filter(lambda x: len(x) >= min_entries, data))
        
        if type in ['mouse_movements', 'mouse']:
            data = [[utils.pad(each['mouseMovements'],n=padding), user] for user in range(len(data))
                for each in data[user]]
            
        elif type in ['kb', 'keystroke_dynamics', 'keyboard']:
            data = [[each['usernameFieldLogs'], each['passwordFieldLogs'], user] for user in range(len(data))
                for each in data[user]]
            
        return data