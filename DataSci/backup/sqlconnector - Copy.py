# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:14:48 2021

@author: John Shumway
"""

import pymysql.cursors

import sys
import os
sys.path.append(os.getcwd())

from TestMessage import TestMessage

class PyMyConnection(object):
    """ CRUD operations for PyMySQL """
    def __init__(self, username, password):
        self.connection = pymysql.connect(
            # create the inital connections
                host='localhost',
                user=username,
                password=password,
                database='school',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        
        #Test cases use the same memory location for Test messages.
        #Creating a type for each catagory of message
        self.TMessage = TestMessage()
        self.ReadTMessage = TestMessage()
    
    """======================================= """
    """---------- CREATE FUCTIONS -------------- """
    
    #Insert a new student (no classes assigned)
    def create_student(self, lastName, firstName, GPA ):
        self.TMessage.resetMessage()
        
        if (lastName is None or firstName is None or GPA is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[create_student]: Error with input parameters')
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `students` (`LastName`, `FirstName`, `GPA`) VALUES ('" + lastName + "', '" + firstName + "','" + str(GPA) + "')"
                cursor.execute(sql)
                id_result = cursor.lastrowid
            self.connection.commit()   
            self.connection.cursor().close()
            #Set the Test Case settings
            self.TMessage.result = True
            self.TMessage.message = '[create_student]: Successfully performed the Student Insert'                  
            self.TMessage.newId = id_result
        
        return self.TMessage
            
    #Insert a new Teacher
    def create_teacher(self, lastName, firstName ):
        self.TMessage.resetMessage()
        
        if (lastName is None or firstName is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[create_teacher]: Error with input parameters')
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `teachers` ( `LastName`, `FirstName`) VALUES ('" + lastName + "', '" + firstName + "')"
                cursor.execute(sql)
                id_result = cursor.lastrowid
            self.connection.commit()   
            self.connection.cursor().close()
            #Set the Test Case settings
            self.TMessage.result = True
            self.TMessage.message = '[create_teacher]: Successfully performed the Teacher Insert'            
            self.TMessage.newId = id_result
        
        return self.TMessage
    
    #Insert a new Class
    def create_class(self, className, studentID, teacherID):
        self.TMessage.resetMessage()
        
        if (className is None or studentID is None or teacherID is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[create_class]: Error with input parameters')
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `classes` ( `studentID`, `teacherID`, className) VALUES ('" + studentID + "', '" + teacherID + "','" + className + "')"
                cursor.execute(sql)
                id_result = cursor.lastrowid
            self.connection.commit()
            self.connection.cursor().close()            
            #Set the Test Case settings
            self.TMessage.result = True
            self.TMessage.message = 'Successfully performed the Teacher Insert'
            self.TMessage.newId = id_result
        
        return self.TMessage
    
    """======================================= """
    """---------- READ FUCTIONS -------------- """
    
    def read_table_byID(self, tableName, IDval):
        #Reset/Re-establish connection to database
        self.ReadTMessage.resetMessage()
        self.connection.ping()
        
        with self.connection.cursor() as cursor:
            # Read a single record
            selected_Table = 'school.' + tableName.strip()
            sql = "SELECT * FROM {} WHERE `id`={}".format(selected_Table, IDval)            
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            self.ReadTMessage.result = True
            self.ReadTMessage.message = '[read_{}_id]: Success!'.format(tableName)
            self.ReadTMessage.json = str(result)
            return self.ReadTMessage        
        
    
    
    def read_student_byID(self, studentID):
        #Reset/Re-establish connection to database
        self.ReadTMessage.resetMessage()
        self.connection.ping()
        
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `students` WHERE `id`=%s"
            cursor.execute(sql, (studentID))
            result = cursor.fetchone()
            cursor.close()
            self.ReadTMessage.result = True
            self.ReadTMessage.message = '[read_student_id]: Success!'
            self.ReadTMessage.json = str(result)
            return self.ReadTMessage
            
    def read_teacher_byID(self, teacherID):          
        #Reset/Re-establish connection to database
        self.ReadTMessage.resetMessage()
        self.connection.ping()
        
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `teachers` WHERE `id`=%s"
            cursor.execute(sql, (teacherID))
            result = cursor.fetchone()
            cursor.close()
            self.ReadTMessage.result = True
            self.ReadTMessage.message = '[read_teacher_id]: Success!'
            self.ReadTMessage.json = str(result)
            return self.ReadTMessage
            
    def read_class_byID(self, classID):
        #Reset/Re-establish connection to database
        self.ReadTMessage.resetMessage()
        self.connection.ping()
        
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `classes` WHERE `id`=%s"
            cursor.execute(sql, (classID))
            result = cursor.fetchone()
            cursor.close()
            self.ReadTMessage.result = True
            self.ReadTMessage.message = '[read_class_id]: Success!'
            self.ReadTMessage.json = str(result)
            return self.ReadTMessage
        #Reset/Re-establish connection to database
        self.ReadTMessage.resetMessage()
        self.connection.ping()
        
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `classes` WHERE `id`=%s"
            cursor.execute(sql, (classID))
            result = cursor.fetchone()
            cursor.close()
            self.ReadTMessage.result = True
            self.ReadTMessage.message = '[read_class_id]: Success!'
            self.ReadTMessage.json = str(result)
            return self.ReadTMessage