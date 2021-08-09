# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:14:48 2021

@author: Avean
"""

import pymysql.cursors

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
    
    
def create_student(self, ):
    with self.connection:
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `students` (`id`, `LastName`, `FirstName`, `GPA`) VALUES ('0002', 'Smith', 'Test', 3.6)"
            cursor.execute(sql)
    
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.connection.commit()
    
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `students` WHERE `id`=%s"
            cursor.execute(sql, ('0001'))
            result = cursor.fetchone()
            print(result)