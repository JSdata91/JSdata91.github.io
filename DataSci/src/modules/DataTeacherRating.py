# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:11:19 2021

@author: John Shumway
"""
import sys
import os
sys.path.append(os.getcwd() + '/..')
sys.path.append(os.getcwd() + '/../tests')

from datetime import datetime
from sqlconnector import PyMyConnection
import matplotlib.pyplot as plt

class TeacherData(object):
    
    def __init__(self, group_id):
        self.group_id = group_id
    
    def RunGraph(self):
        #=======================
        # Pre-setup
        timestamp = datetime.now()
        str_tstamp = timestamp.strftime("%d%m%Y-%H%M%S")
        
        
        Teacher_lst = []
        

        chart_path = ".\charts\\"
        fileName_RatingPay = chart_path + 'Teacher_RatingPay_' + str_tstamp + '.png'
        fileName_PayYears = chart_path + 'Teacher_PayOverYears_' + str_tstamp + '.png'
        fileName_RatingOverYears = chart_path + 'Teacher_RatingOverYears_' + str_tstamp + '.png'
        group_id = self.group_id
        

        
        #=======================
        # Main
        
        mysql_conn = PyMyConnection("admin", "admin")
        
        #Read all student's GPA
        teachers = mysql_conn.read_allTeachers()
        for teach in teachers:
            teacherName =  teach.get('firstName') + ',' + teach.get('lastName')
            teacherPay = teach.get('salary')
            teacherRate = teach.get('rating')  
            teacherYears = teach.get('yearsEmployeed')  #need to fix name
            Teacher_lst.append([teacherName, teacherPay, teacherRate, teacherYears])  
            
        
            
        #=======================
        #Generate Scatter Plots
        def ScatterOnTeacherRaitingPay():
            x = []
            y = []
            for tlist in Teacher_lst:
                x.append(tlist[1])
                y.append(tlist[2])
            
            colors = 'green'
            area = 22
            
            plt.scatter(x, y, s=area, c=colors, alpha=0.5)
            plt.title('Teacher Rating vs Pay')
            plt.xlabel('Pay')
            plt.ylabel('Student Rating')
            plt.savefig(fileName_RatingPay, format='png')
            mysql_conn.create_dataBlob(fileName_RatingPay, fileName_RatingPay, group_id)
            plt.show()
            
        def ScatterOnTeacherPayYears():
            x = []
            y = []
            for tlist in Teacher_lst:
                x.append(tlist[3])
                y.append(tlist[1])
            
            colors = 'orange'
            area = 22
            
            plt.scatter(x, y, s=area, c=colors, alpha=0.5)
            plt.title('Teacher Pay vs Years Employed')
            plt.xlabel('Years Employed')
            plt.ylabel('Pay')
            plt.savefig(fileName_PayYears, format='png')
            mysql_conn.create_dataBlob(fileName_PayYears, fileName_PayYears, group_id)
            plt.show()
            
        def ScatterOnTeacherRaitingYears():
            x = []
            y = []
            for tlist in Teacher_lst:
                x.append(tlist[3])
                y.append(tlist[2])
            
            colors = 'teal'
            area = 22
            
            plt.scatter(x, y, s=area, c=colors, alpha=0.5)
            plt.title('Teacher Rating vs Years Employed')
            plt.xlabel('Years Employed')
            plt.ylabel('Student Rating')
            plt.savefig(fileName_RatingOverYears, format='png')
            mysql_conn.create_dataBlob(fileName_RatingOverYears, fileName_RatingOverYears, group_id)
            plt.show()
        
        ScatterOnTeacherRaitingPay()
        ScatterOnTeacherRaitingYears()
        ScatterOnTeacherPayYears()