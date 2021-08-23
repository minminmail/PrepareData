# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import numpy as np
import os


class GenerateData:
    
    # disjunct x
    x_min=None
    x_max=None
    
     # disjunct y
    y_min=None
    y_max=None
    number =None
    
    x_array = None
    y_array = None
    
    class_type = None
    
     # store x_array and  y_array
    value_array = None
    

    dir_current ="C:/phd_algorithms/datasets_2021/prepare_draw/read_draw/dataset"
    
    def __init__(self,x_min,x_max,y_min,y_max,number,class_type):
       
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.number = number
        self.class_type = class_type
        
    def generate(self):
    
        # small disjunct one
        x_array= np.array( np.random.uniform(self.x_min, self.x_max, self.number))
        np.set_printoptions(precision=1)
         # print(x_array)
        y_array= np.array( np.random.uniform(self.y_min, self.y_max, self.number))
         # print(y_array)
        
        self.value_array =[x_array,y_array]       
        return self.value_array
        
    def save_data(self,x_array,y_array,class_type,data_file,new_file):
        
        file_path= os.path.join(self.dir_current,data_file)
        
        print(file_path)
        print("begin save_data :")
        if new_file:
            file = open(file_path,"w",encoding="UTF-8")   
        else:
            file = open(file_path,"a",encoding="UTF-8")   
        print(file)
        x_size = len(x_array)
        y_size = len(y_array)
        
        line_string =""        
        if x_size == y_size:
            
            for i in range(0,x_size):
                line_string =line_string + str(x_array[i])+","+ str(y_array[i])+","+class_type+"\n"
        
        print("the line string will be saved into file :")
        #print(line_string)
      
        file.write(line_string)
        file.close() 
        print("finished save_data :")
        
        
    
    
