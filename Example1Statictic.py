# -*- coding: utf-8 -*-
from MaxMin import MaxMin
import os

class Example1Statictic:
    
    fileName = None
    file_path = None

    
    if __name__ == "__main__":
        
        fileName = "tst.dat "
        dir_current ="C:/phd_algorithms/datasets_2021/prepare_draw/read_draw/dataset"
        file_path= os.path.join(dir_current,fileName)
        
        maxMin = MaxMin(file_path)
        maxMin.get_max_min()