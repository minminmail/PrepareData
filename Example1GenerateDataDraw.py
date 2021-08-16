# -*- coding: utf-8 -*-

from GenerateData import GenerateData
from Draw import Draw
import matplotlib.pyplot as plt
import os

class Example1GenerateDataDraw:
    

     
    def generate_disjunct(draw_instance, fig,ax, x_min,x_max,y_min,y_max,number,class_type,data_file,new_file,category_new_file):
        
 
        data_red =  'data_red.dat'
        data_green =  'data_green.dat'
         
        print("Before the generate data in GenerateData")
        generate = GenerateData(x_min,x_max,y_min,y_max,number,class_type)
        value_array = generate.generate()
        print("after the generate data in GenerateData")
        #print(value_array)
        #print(value_array[0])
        #print(value_array[1])
        
        x_array = value_array[0]
        y_array = value_array[1]
        
        paint_shape= None
        paint_color = None
        category_file = None
        

        if class_type =="red":
            paint_shape='^'
            paint_color = 'red'
            category_file = data_red
        else:
            paint_shape='o'
            paint_color = 'green'
            category_file = data_green
            
        # draw_instance.paint_with_arrays(fig,ax,x_array,y_array,paint_shape, paint_color)

        # x_array,y_array,class_type,data_file
        generate.save_data(x_array,y_array,class_type,data_file,new_file)
        generate.save_data(x_array,y_array,class_type,category_file,category_new_file)
    
    
    if __name__ == "__main__":
        
        fig, ax = plt.subplots()
        draw =Draw()
        data_file = 'data1.dat'
        data_red =  'data_red.dat'
        data_green =  'data_green.dat'
        
        # small disjunct one
        x1_min=9
        x1_max=11
        y1_min=14
        y1_max=16
        number1=11
        class_type1="red"
        new_file = True
        category_new_file = True
        
        generate_disjunct(draw,fig,ax, x1_min,x1_max,y1_min,y1_max,number1,class_type1,data_file,new_file,category_new_file )
        
        # small disjunct two
        x2_min=2.1
        x2_max=4
        y2_min=6
        y2_max=8
        number2=12
        class_type2="red"
        new_file = False
        category_new_file = False
        generate_disjunct(draw,fig,ax,x2_min,x2_max,y2_min,y2_max,number2,class_type2,data_file,new_file,category_new_file )
        
    
        # small disjunct three
        x3_min=11
        x3_max=13
        y3_min=3
        y3_max=4
        number3=9
        class_type3="red"
        new_file = False
        category_new_file = False
        generate_disjunct(draw,fig,ax,x3_min,x3_max,y3_min,y3_max,number3,class_type3,data_file,new_file,category_new_file )
        
            # big  disjunct one
        x4_min=0
        x4_max=16
        y4_min=0
        y4_max=16
        number4=300
        class_type4="green"
        new_file = False
        category_new_file = True
        generate_disjunct(draw,fig,ax,x4_min,x4_max,y4_min,y4_max,number4,class_type4,data_file,new_file,category_new_file )
        
        
        draw.set_read_files(data_green,data_red)
        draw.paint()
   
    

