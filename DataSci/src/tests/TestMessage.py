# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:46:24 2021

@author: John Shumway
"""

class TestMessage(object):
    def __init__(self):
        self.result = False
        self.message = "n/a"
        self.newId = 0
        self.json = ""
           
    
    def resetMessage(self):
        self.result = False
        self.message = 'n/a'
        self.newId = 0
        self.json = ""