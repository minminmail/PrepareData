# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from MaxMin import MaxMin
from pathlib import Path

class Example1Statictic:
    
    fileName = None
    file_path = None
    


    
    if __name__ == "__main__":
        
        dataset_folder = 'A3'
        data_folder = 'dataset'
        cwd = Path.cwd()

        file_valid_name = None
        # data_file =  cwd / dataset_folder / data_folder /'data3.dat'
        
        data_file =  cwd /dataset_folder/'data3Keel-10-1tra.dat'   
        maxMin = MaxMin(data_file)
        maxMin.get_max_min()