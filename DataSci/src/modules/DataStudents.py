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
import numpy as np

class StudentData(object):
    def __init__(self, group_id):
        self.group_id = group_id
    
    def RunGraph(self):
        #=======================
        # Pre-setup
        timestamp = datetime.now()
        str_tstamp = timestamp.strftime("%d%m%Y-%H%M%S")
        chart_path = ".\charts\\"
        fileName = chart_path + 'GPAOverview_' + str_tstamp + '.png'
        majors_lst = []
        group_id = self.group_id
        
        file1 = open('../lib/Majors.txt', 'r')
        Lines = file1.readlines()
        
        #Create a row of GPA counts for each major.  Strip the return character.
        for line in Lines:
            if line not in majors_lst:        
                majors_lst.append([line.rstrip(), 0, 0, 0, 0, 0])
        
        #sort results
        majors_lst.sort()
        
        #=======================
        # Main
        
        mysql_conn = PyMyConnection("admin", "admin")
        
        #Read all student's GPA
        students = mysql_conn.read_studentGPA()
        for st in students:
            #get ID of Major name
            index = 0
            for major in majors_lst:
                if st.get('Major') == major[0]:
                    break
                else:
                    index += 1
            
            
            
            #Check Student's GPA and add to the correct list
            GPA = st.get('GPA')
            if (GPA < 2.0):
                majors_lst[index][1] = majors_lst[index][1] + 1
            elif (GPA < 2.6):
                majors_lst[index][2] = majors_lst[index][2] + 1
            elif (GPA < 3.0):
                majors_lst[index][3] = majors_lst[index][3] + 1
            elif (GPA < 3.5):
                majors_lst[index][4] = majors_lst[index][4] + 1
            elif (GPA <= 4.0):
                majors_lst[index][5] = majors_lst[index][5] + 1
                
                
        #Create a Horizontal Chart for GPA
        fig, ax = plt.subplots()
        
        #Populate Data
        category_names = ['Below 2.0 GPA', '2.1-2.5 GPA', '2.6-3.0 GPA', '3.1-3.5 GPA', '3.6-4.0 GPA']
        res_dct = {}
        for major in majors_lst:
            res_dct[major[0]] = major[1:6]
            
        
        def dataGraph(results, category_names):
            labels = list(results.keys())
            data = np.array(list(results.values()))
            data_cum = data.cumsum(axis=1)
            category_colors = plt.get_cmap('Spectral')(
                np.linspace(0.06, 0.86, data.shape[1]))
            
            fig, ax = plt.subplots(figsize=(9.2, 5))
            ax.invert_yaxis()
            ax.xaxis.set_visible(False)
            ax.set_xlim(0, np.sum(data, axis=1).max())
            
            for i, (colname, color) in enumerate(zip(category_names, category_colors)):
                    widths = data[:, i]
                    starts = data_cum[:, i] - widths
                    rects = ax.barh(labels, widths, left=starts, height=0.5,
                                    label=colname, color=color)
            
                    r, g, b, _ = color
                    text_color = 'black' if r * g * b > 0.15 else 'white'
                    ax.bar_label(rects, label_type='center', color=text_color, size=8)
            ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
                      loc='lower left', fontsize='small')
            
            plt.savefig(fileName, format='png', dpi=fig.dpi)
            mysql_conn.create_dataBlob(fileName, fileName, group_id)
            plt.show()
            
        
        dataGraph(res_dct, category_names)