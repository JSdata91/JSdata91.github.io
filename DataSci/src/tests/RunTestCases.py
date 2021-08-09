# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 23:25:29 2021

@author: John Shumway
"""

import sys
import os
sys.path.append(os.getcwd() + '/..')

#import test cases
import TestStudent
import TestTeacher
from TestClass import TestCaseClass

class TestClass(object):
    def RunTestCases(self):
        # Init Test Cases
        caseResults = [False, False, False]
        
        CaseStudent = TestStudent.TestCaseStudent()
        CaseTeacher = TestTeacher.TestCaseTeacher()
        CaseClass = TestCaseClass()
        
        #Run Tests
        caseResults[0] = CaseStudent.RunTest()
        caseResults[1] = CaseTeacher.RunTest()
        caseResults[2] = CaseClass.RunTest()
        
        
        if False in caseResults:
            return False
        else:
            return True