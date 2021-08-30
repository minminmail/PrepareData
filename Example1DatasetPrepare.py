# -*- coding: utf-8 -*-


from SeperateTraTst import SeperateTraTst
import os

class Example1DatasetPrepare:
    
    data_file ="data1.dat"
    tra_file ="tra.dat"
    tst_file ="tst.dat"
    
    dir_current ="C:/phd_algorithms/datasets_2021/prepare_draw/read_draw/dataset"
    origin_file_path= os.path.join(dir_current,data_file)
    tra_file_path= os.path.join(dir_current,tra_file)
    tst_file_path= os.path.join(dir_current,tst_file)
    
    
    if __name__ == "__main__":
        
         seperateTraTst = SeperateTraTst(origin_file_path,tra_file_path,tst_file_path)
         seperateTraTst.seperate()