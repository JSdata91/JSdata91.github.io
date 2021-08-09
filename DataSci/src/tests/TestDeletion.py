# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:06:08 2021

@author: John Shumway
"""
import sys
import os
sys.path.append(os.getcwd() + '/..')

from sqlconnector import PyMyConnection
from TestMessage import TestMessage

class TestCaseClass(object):
    def __init__(self):
        # ==================================
        # Init Database connection
        # TODO: better security in password
        self.my_sqlconnector = PyMyConnection('admin', 'admin')
        self.checklst = []
    
    def RunTest(self):
        # ==================================
        #Test Class creation
        class_id = 28
        teacher_id = 55
        student_id = 55