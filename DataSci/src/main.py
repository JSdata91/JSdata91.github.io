# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 23:25:28 2021

@author: John Shumway
"""

from modules.DataStudents import StudentData
from modules.DataMajorPercentPie import MajorData
from modules.DataClassGPAPie import ClassData
from modules.DataTeacherRating import TeacherData
from modules.ChartRetrieval import ChartRetrieval
from tests.RunTestCases import TestClass

#-------------------------
# Setup
lst_modules = [
    "Student's GPA", 
    "Major & GPA", 
    "Class Data", 
    "Teacher Staticics", 
    "Run All Graphs", 
    "Get Chart", 
    "Run Unit Tests",
    "Exit"]
count = 1

#-------------------------
# MAIN


#Bring up the Module List
for module_item in lst_modules:
    print(str(count) + ": " + str(module_item) )
    count += 1
    
user_module_selection = int(input("Select a Module: "))
module_selection = lst_modules[user_module_selection - 1]

user_group_id = input("Enter Group ID: ")

#-------------------------
#Select Mddule to run.
if module_selection == "Student's GPA":
    module_studentData = StudentData(user_group_id)
    module_studentData.RunGraph()
    
elif module_selection == "Major & GPA":
    module_majorData = MajorData(user_group_id)
    module_majorData.RunGraph()
    
elif module_selection == "Class Data":
    module_classData = ClassData(user_group_id)
    module_classData.RunGraph()
    
elif module_selection == "Teacher Staticics":
    module_teacherData = TeacherData(user_group_id)
    module_teacherData.RunGraph()
    
elif module_selection == "Get Chart":
    module_chartData = ChartRetrieval(user_group_id)
    module_chartData.GetGraph()
    
elif module_selection == "Run All Graphs":
    #Run All new-chart items
    module_studentData = StudentData(user_group_id)
    module_majorData = MajorData(user_group_id)
    module_teacherData = TeacherData(user_group_id)
    module_classData = ClassData(user_group_id)

    module_studentData.RunGraph()
    module_classData.RunGraph()
    module_majorData.RunGraph()
    module_teacherData.RunGraph()
    
elif module_selection == "Run Unit Tests":
    module_testCases = TestClass()
    module_testCases.RunTestCases()
    