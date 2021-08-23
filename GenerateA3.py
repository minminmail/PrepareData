# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from GenerateData import GenerateData
from Draw import Draw
import matplotlib.pyplot as plt
from pathlib import Path

class GenerateA3:
    

    file_valid_name = None
 
    
    def generate_disjunct(draw_instance, fig,ax, x_min,x_max,y_min,y_max,number,class_type,data_file,new_file,category_new_file):
        
        dataset_folder = 'A3'
        data_folder = 'dataset'

        cwd = Path.cwd()
        data_file =  cwd / dataset_folder / data_folder / 'data3.dat'
        data_red =  cwd / dataset_folder / data_folder / 'data_red3.dat'
        data_green =  cwd / dataset_folder / data_folder / 'data_red3.dat'
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
        generate.save_data(x_array,y_array,class_type,data_file,category_new_file)
        generate.save_data(x_array,y_array,class_type,category_file,category_new_file)
    
    
    if __name__ == "__main__":
        
        fig, ax = plt.subplots()
        draw =Draw()
        data_file = 'data3.dat'
     
        
        # small disjunct one
        x1_min=3.6
        x1_max=3.8
        y1_min=10
        y1_max=11.8
        number1=16
        class_type1="red"
        new_file = True
        category_new_file = True
        
        generate_disjunct(draw,fig,ax, x1_min,x1_max,y1_min,y1_max,number1,class_type1,data_file,new_file,category_new_file )
        
        # small disjunct two
        x2_min=12.2
        x2_max=12.4
        y2_min=7.6
        y2_max=7.8
        number2=23
        class_type2="red"
        new_file = False
        category_new_file = False
        generate_disjunct(draw,fig,ax,x2_min,x2_max,y2_min,y2_max,number2,class_type2,data_file,new_file,category_new_file )
        
    
        
            # big  disjunct one
        x4_min=0
        x4_max=16
        y4_min=0
        y4_max=16
        number4=960
        class_type4="green"
        new_file = False
        category_new_file = True
        generate_disjunct(draw,fig,ax,x4_min,x4_max,y4_min,y4_max,number4,class_type4,data_file,new_file,category_new_file )
        
        
        draw.set_read_files(data_green,data_red)
        draw.paint()
   
    


