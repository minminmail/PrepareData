# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd 
import os

class Draw:
    
    

    greenFile="C:\phd_algorithms\datasets_2021\A1\data_green.dat"
    redFile="C:\phd_algorithms\datasets_2021\A1\data_red.dat"
    dir_current ="C:/phd_algorithms/datasets_2021/prepare_draw/read_draw/dataset"

    
    def __init__(self):     
       pass
        
    def set_read_files(self,greenFile,redFile):
       
        self.greenFile = greenFile
        self.redFile = redFile
        
    def paint(self):
        print("begin to paint")
        
        file_path1= os.path.join(self.dir_current,self.greenFile)
            
        df = pd.read_csv(file_path1,names=["x", "y", "class"])    
        plt.rcParams['figure.figsize']=(6,4)
        plt.rcParams['figure.dpi']=150
        
        
        columnx = df['x']
        columny = df['y']
        
        fig, ax = plt.subplots()
        ax.scatter(columnx, columny,marker='o', color='g', s=50) 
        
        file_path2= os.path.join(self.dir_current,self.redFile)
        df = pd.read_csv(file_path2,names=["x", "y", "class"]) 
        columnx = df['x']
        columny = df['y']
        
        ax.scatter(columnx, columny,marker='^', color='r', s=50) 
        
        line_y1=4
        line_y2=8
        line_y3=12
        x1_values=[0,16]
        y1_values=[ line_y1,line_y1]
        
        plt.plot(x1_values, y1_values,'b')
        
        x2_values=[0,16]
        y2_values=[ line_y2,line_y2]
        
        plt.plot(x2_values, y2_values,'b')
        
        x3_values=[0,16]
        y3_values=[ line_y3,line_y3]
        
        plt.plot(x3_values, y3_values,'b')
        
        
        x1_v_values=[4,4]
        y1_v_values=[ 0,16]
        
        plt.plot(x1_v_values, y1_v_values,'b')
        
        
        x2_v_values=[8,8]
        y2_v_values=[ 0,16]
        
        plt.plot(x2_v_values, y2_v_values,'b')
        
        x3_v_values=[12,12]
        y3_v_values=[ 0,16]
        
        plt.plot(x3_v_values, y3_v_values,'b')
        
        plt.show()
        print("Finished to paint")
        
    def paint_with_arrays(self,fig, ax, columnx,columny,paint_shape, paint_color):
        
        print("begin to paint with arrays parameters")
     
        ax.scatter(columnx, columny,marker= paint_shape, color= paint_color, s=50)        
        plt.show()
        print("Finished to paint_with_arrays")
        
            
    def paint_grid(self,fig, ax):
        
        print("begin to paint_grid ")
        
        line_y1=4
        line_y2=8
        line_y3=12
        x1_values=[0,16]
        y1_values=[ line_y1,line_y1]
        
        plt.plot(x1_values, y1_values,'b')
        
        x2_values=[0,16]
        y2_values=[ line_y2,line_y2]
        
        plt.plot(x2_values, y2_values,'b')
        
        x3_values=[0,16]
        y3_values=[ line_y3,line_y3]
        
        plt.plot(x3_values, y3_values,'b')
        
        
        x1_v_values=[4,4]
        y1_v_values=[ 0,12]
        
        plt.plot(x1_v_values, y1_v_values,'b')
        
        
        x2_v_values=[8,8]
        y2_v_values=[ 0,12]
        
        plt.plot(x2_v_values, y2_v_values,'b')
        
        x3_v_values=[12,12]
        y3_v_values=[ 0,12]
        
        plt.plot(x3_v_values, y3_v_values,'b')
        
        plt.show()
        print("Finished to paint_grid")