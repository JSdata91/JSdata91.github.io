# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:18:56 2021

@author: John Shumway
"""
import sys
import os
sys.path.append(os.getcwd() + '/..')

from sqlconnector import PyMyConnection
from TestMessage import TestMessage
import copy

class TestCaseTeacher(object):
    def __init__(self):
        # ==================================
        # Init Database connection
        # TODO: better security in password
        self.my_sqlconnector = PyMyConnection('admin', 'admin')
        self.checklst = []
        
    def RunTest(self): 
        # ==================================
        #Test Teacher creation
        teacher_FName = 'Nancy'
        teacher_LName = 'Teacher'
        teacher_Years = 8
        teacher_Pay = 77000
        teacher_Rating = 3.7
        teacher_Rating_New = 4.5
        
        # ==================================
        #Create Test Cases.   Insert the new Teacher, then read the db on the new index to confirm the data is correct
        TC_createTeacher = copy.deepcopy(self.my_sqlconnector.create_teacher(teacher_LName, teacher_FName, teacher_Years, teacher_Pay, teacher_Rating) )
        TC_readTeacher = copy.deepcopy(self.my_sqlconnector.read_table_byID("teachers", TC_createTeacher.newId) )
        TC_createTeacher_update = copy.deepcopy( self.my_sqlconnector.update_teacher_rating(TC_createTeacher.newId, str(teacher_Rating_New)) )
        TC_readTeacher_update = copy.deepcopy( self.my_sqlconnector.read_table_byID("teachers", TC_createTeacher.newId) )
               
        
        self.checklst.append(TC_createTeacher)
        self.checklst.append(TC_readTeacher)
        self.checklst.append(TC_createTeacher_update)
        self.checklst.append(TC_readTeacher_update)
        
        string_correct_json = "{{'id': {idnum}, 'lastName': 'Teacher', 'firstName': 'Nancy', 'yearsEmployeed': 8, 'salary': 77000, 'rating': 3.7}}".format(idnum = TC_createTeacher.newId)
        string_correct_json_update = "{{'id': {idnum}, 'lastName': 'Teacher', 'firstName': 'Nancy', 'yearsEmployeed': 8, 'salary': 77000, 'rating': 4.5}}".format(idnum = TC_createTeacher.newId)
        
        # ===================================
        # Check results of tests.
        
        flg_Test_Result = True
        
        if TC_readTeacher.json == string_correct_json:
            print('Teacher Tests Successful!')
        else:
            print('Error found with Teacher Tests!')
            print('   JSON: ' + TC_readTeacher.json)
            print('   Correct Answer: ' + string_correct_json)  
            flg_Test_Result = False
            
        if TC_readTeacher_update.json == string_correct_json_update:
            print('Teacher Tests Update Successful!')
        else:
            print('Error found with Teacher Test Update!')
            print('   JSON: ' + TC_readTeacher_update.json)
            print('   Correct Answer: ' + string_correct_json_update)  
        
            flg_Test_Result = False
            
        return flg_Test_Result           
