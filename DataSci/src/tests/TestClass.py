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
        class_Name = 'Programming 101'
        
        
        #Test Student creation
        student_FName = 'Joe'
        student_LName = 'McTest'
        student_GPA = 2.6
        student_Major = 'Art'
        
        #Test Teacher creation
        teacher_FName = 'Nancy'
        teacher_LName = 'Teacher'
        teacher_Years = 8
        teacher_Pay = 77000
        teacher_Rating = 3.7
        
        teacher_FName2 = 'Mary'
        teacher_LName2 = 'Classroom'
        teacher_Years2 = 3
        teacher_Pay2 = 56000
        teacher_Rating2 = 4.1
        
        # ==================================
        #Create Test Cases.   Insert the new Class, then read the db on the new index to confirm the data is correct
        #Need new IDs for Student and Teacher
        TC_createStudent = copy.deepcopy(self.my_sqlconnector.create_student(student_LName, student_FName, student_GPA, student_Major) )
        TC_createTeacher = copy.deepcopy(self.my_sqlconnector.create_teacher(teacher_LName, teacher_FName, teacher_Years, teacher_Pay, teacher_Rating) )
        TC_createTeacher2 = copy.deepcopy(self.my_sqlconnector.create_teacher(teacher_LName2, teacher_FName2, teacher_Years2, teacher_Pay2, teacher_Rating2) )

        
        TC_createClass = copy.deepcopy(self.my_sqlconnector.create_class(class_Name, str(TC_createStudent.newId), str(TC_createTeacher.newId)) )
        TC_readClass = copy.deepcopy(self.my_sqlconnector.read_table_byID("classes", TC_createClass.newId) )
        TC_updateClass = copy.deepcopy(self.my_sqlconnector.update_class_teacher(str(TC_createClass.newId), str(TC_createTeacher2.newId)) )
        TC_readClass_update = copy.deepcopy(self.my_sqlconnector.read_table_byID("classes", str(TC_createClass.newId)) )

        
        string_correct_json = "{{'id': {idnum}, 'studentid': {idStu}, 'teacherid': {idTeach}, 'className': 'Programming 101'}}".format(idnum = TC_createClass.newId, idStu = TC_createStudent.newId, idTeach = TC_createTeacher.newId )
        string_correct_json_update = "{{'id': {idnum}, 'studentid': {idStu}, 'teacherid': {idTeach}, 'className': 'Programming 101'}}".format(idnum = TC_createClass.newId, idStu = TC_createStudent.newId, idTeach = TC_createTeacher2.newId)
        
        
        # ===================================
        # Check results of tests.
        
        flg_Test_Result = True
        
        if TC_readClass.json == string_correct_json:
            print('Class Tests Successful!')
        else:
            print('Error found with Class Tests!')
            print('   JSON: ' + TC_readClass.json)
            print('   Correct Answer: ' + string_correct_json)     
            flg_Test_Result = False
        
        if TC_readClass_update.json == string_correct_json_update:
             print('Class Tests Update Successful!')
        else:
            print('Error found with Class Test Update!')
            print('   JSON: ' + TC_readClass_update.json)
            print('   Correct Answer: ' + string_correct_json_update)
            flg_Test_Result = False
            
        return flg_Test_Result          