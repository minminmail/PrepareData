# -*- coding: utf-8 -*-
import pandas as pd 

class SeperateTraTst:
    
    
       # traFile = "C:\phd_algorithms\datasets_2021\A1\tra.dat"
       # tstFile = 'C:\phd_algorithms\datasets_2021\A1\tst.dat'
       # originFile = "C:\phd_algorithms\datasets_2021\A1\data.dat"
    
       def __init__(self,originFile,traFile,tstFile):
            self.originFile = originFile
            self.traFile = traFile
            self.tstFile = tstFile

        
       def seperate(self):
            df = pd.read_csv(self.originFile) 
            print(df)
            training_data = df.sample(frac=0.8, random_state=25)
            testing_data = df.drop(training_data.index)
            
            print(f"No. of training examples: {training_data.shape[0]}")
            print(f"No. of testing examples: {testing_data.shape[0]}")
            
            print(self.traFile)
            print(self.tstFile)
            training_data.to_csv(self.traFile,header=["f1", "f2", "class"], index=None, sep=',', mode='w')
            testing_data.to_csv(self.tstFile, header=["f1", "f2", "class"], index=None, sep=',', mode='w')