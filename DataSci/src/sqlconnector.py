# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:14:48 2021

@author: John Shumway
"""

import pymysql.cursors

import sys
sys.path.insert(0, './tests')
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
    def create_student(self, lastName, firstName, GPA, Major ):
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if (lastName is None or firstName is None or GPA is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[create_student]: Error with input parameters')
            
            return self.TMessage
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `students` (`LastName`, `FirstName`, `GPA`, `Major`) VALUES ('" + lastName + "', '" + firstName + "', '" + str(GPA) + "', '" + Major + "')"
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
    def create_teacher(self, lastName, firstName, years, pay, rating ):
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if (lastName is None or firstName is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[create_teacher]: Error with input parameters')
            
            return self.TMessage
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `teachers` ( `LastName`, `FirstName`, `yearsEmployeed`, `salary`, `rating`) VALUES ('" + lastName + "', '" + firstName + "', '" + str(years) + "', '" + str(pay) + "', '" + str(rating) + "')"
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
        self.connection.ping()
        
        if (className is None or studentID is None or teacherID is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[create_class]: Error with input parameters')
            
            return self.TMessage
            
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
    
    
    #Insert a new png image
    def create_dataBlob(self, image_name, image_url, group_id):
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if(image_name is None or image_url is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[create_dataBlob]: Error with input parameters')
                             
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql_insert_blob_query = """ INSERT INTO school.charts
                                  (GroupCode, FileName, ChartData) VALUES (%s,%s,%s)"""
                                  
                    with open(image_url, 'rb') as file:
                        binaryData = file.read()
                        
                    # Convert data into tuple format
                    insert_blob_tuple = (group_id, image_name, binaryData)
                    cursor.execute(sql_insert_blob_query, insert_blob_tuple)
                    self.connection.commit()
                    self.connection.cursor().close() 
                    self.TMessage.message = 'Successfully performed the BLOB Insert'
                    return self.TMessage                    
                    
        except self.connection.Error as error:
           print("Failed inserting BLOB data into MySQL table {}".format(error))
            
    """======================================= """
    """---------- READ FUCTIONS -------------- """
    
    def read_allMajors(self):
        self.ReadTMessage.resetMessage()
        self.connection.ping()
        
        with self.connection.cursor() as cursor:
            # Read a single record
            selected_Table = 'school.students'
            sql = "SELECT DISTINCT Major FROM {}".format(selected_Table)            
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
    
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
        
    def read_studentGPA(self):
        self.ReadTMessage.resetMessage()
        self.connection.ping()
        
        with self.connection.cursor() as cursor:
            # Read a single record
            selected_Table = 'school.students'
            sql = "SELECT FirstName, LastName, GPA, Major FROM {}".format(selected_Table)            
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
        
    def read_allTeachers(self):
        self.ReadTMessage.resetMessage()
        self.connection.ping()
        
        with self.connection.cursor() as cursor:
            # Read a single record
            selected_Table = 'school.teachers'
            sql = "SELECT * FROM {}".format(selected_Table)            
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
        
    def read_charts_by_group(self, group_id):
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if(group_id is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[read_charts_by_group]: Error with input parameters')
                             
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = "SELECT * FROM school.charts WHERE GroupCode={}".format(group_id)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    cursor.close()  
                    return result
                
        except self.connection.Error as error:
           print("Failed reading BLOB data from MySQL table {}".format(error))
        
        
    def read_chart_to_file(self, chartID, newFilename):
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if(chartID is None or newFilename is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[read_dataBlob]: Error with input parameters')
                             
        try:
            with self.connection:
                with self.connection.cursor() as cursor:
                    sql = "SELECT ChartData FROM school.chart WHERE id={}".format(chartID)
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    cursor.close()  
                    
                    #create file with the BLOB data
                    with open(newFilename, 'wb') as file:
                        file.write(data)
                        
        except self.connection.Error as error:
           print("Failed reading BLOB data from MySQL table {}".format(error))
        
    """======================================= """
    """--------- UPDATE FUCTIONS ------------- """
    
    def update_student_name(self, student_id, new_firstName, new_lastName):
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if (new_firstName is None or new_lastName is None or student_id is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[update_student_name]: Error with input parameters')
            
            return self.TMessage
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Update a new record
                sql = "UPDATE School.student set FirstName = {}, LastName = {}  where id={}".format(new_firstName, new_lastName, student_id ) 
                cursor.execute(sql)
                id_result = cursor.lastrowid
            self.connection.commit()   
            self.connection.cursor().close()
            #Set the Test Case settings
            self.TMessage.result = True
            self.TMessage.message = '[update_student_name]: Successfully performed the Student Update'
        
        return self.TMessage
    
    def update_student_GPA(self, student_id, new_GPA):
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if (new_GPA is None or student_id is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[update_student_gpa]: Error with input parameters')            
            return self.TMessage
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Update a new record
                sql = "UPDATE School.students set GPA = {} where id={}".format(new_GPA, student_id ) 
                cursor.execute(sql)
                id_result = cursor.lastrowid
            self.connection.commit()   
            self.connection.cursor().close()
            #Set the Test Case settings
            self.TMessage.result = True
            self.TMessage.message = '[update_student_name]: Successfully performed the Student Update'
        
        return self.TMessage
    
    def update_class_teacher(self, class_id, teacher_id):
        #expected that Teacher id was validated before this function
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if (class_id is None or teacher_id is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[update_class_teacher]: Error with input parameters')            
            return self.TMessage
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Update a new record
                sql = "UPDATE School.classes set teacherid = {}  where id={}".format(teacher_id, class_id ) 
                cursor.execute(sql)
                id_result = cursor.lastrowid
            self.connection.commit()   
            self.connection.cursor().close()
            #Set the Test Case settings
            self.TMessage.result = True
            self.TMessage.message = '[update_class_teacher]: Successfully performed the Student Update'
        
        return self.TMessage
    
    def update_teacher_rating(self, teacher_id, new_rating):
        self.TMessage.resetMessage()
        self.connection.ping()
        
        if (teacher_id is None or new_rating is None):
            self.TMessage.result = False
            self.TMessage.setMessage('[update_teacher_rating]: Error with input parameters')            
            return self.TMessage
            
        with self.connection:
            with self.connection.cursor() as cursor:
                # Update a new record
                sql = "UPDATE School.teachers set rating = {} where id={}".format(new_rating, teacher_id ) 
                cursor.execute(sql)
            self.connection.commit()   
            self.connection.cursor().close()
            #Set the Test Case settings
            self.TMessage.result = True
            self.TMessage.message = '[update_teacher_rating]: Successfully performed the Student Update'
        
        return self.TMessage        
    