# -*- coding: utf-8 -*-
from ReadDataSet import ReadDataSet
import os
from pathlib import Path

class SDIRAF:
    
    big_disjunct_class_accuracy = 0
    small_disjunct_class_accuracy = 0
    big_disjunct_instance_number = 0
    small_disjunct_instance_number= 0
    big_disjunct_predict_correct_number= 0
    small_disjunct_predict_correct_number= 0
    big_disjunct_class = 'green'
    small_disjunct_class= 'red'
    
    result_file =None
    
    def __init__(self):
        pass
  
    def calculatSDIRAF(self,result_file):
        
        self.big_disjunct_class_accuracy = 0
        self.small_disjunct_class_accuracy = 0
        self.big_disjunct_instance_number = 0
        self.small_disjunct_instance_number= 0
        self.big_disjunct_predict_correct_number= 0
        self.small_disjunct_predict_correct_number= 0
        self.result_file = result_file


        readDataSet = ReadDataSet()
        dataFrame = readDataSet.read_result_data_file(result_file)
        # We write the output for each example
        for i in range(0, len(dataFrame)):
            # for classification:
            output= "" 
            original_class = dataFrame.loc[i,0]
            print("original_class :"+str(original_class))
            predict_class =dataFrame.loc[i,1]

            output = output + original_class + " " + predict_class+ "\n"
            if original_class == self.big_disjunct_class:
                self.big_disjunct_instance_number = self.big_disjunct_instance_number + 1
                if predict_class == original_class:
                    self.big_disjunct_predict_correct_number = self.big_disjunct_predict_correct_number + 1
            elif original_class == self.small_disjunct_class:
                self.small_disjunct_instance_number = self.small_disjunct_instance_number + 1
                if predict_class == original_class:
                    self.small_disjunct_predict_correct_number = self.small_disjunct_predict_correct_number + 1

        if os.path.isfile(result_file):
            # print("File exist")
            output_file = open(result_file, "a+")
        else:
            # print("File not exist")
            output_file = open(result_file, "w+")
        print("self.big_disjunct_instance_number :"+str(self.big_disjunct_instance_number))

        self.big_disjunct_class_accuracy = self.big_disjunct_predict_correct_number/self.big_disjunct_instance_number
        self.small_disjunct_class_accuracy = self.small_disjunct_predict_correct_number/self.small_disjunct_instance_number
        self.imbalance_rate = self.big_disjunct_instance_number/self.small_disjunct_instance_number
        percentage_ir = self.big_disjunct_instance_number/(self.big_disjunct_instance_number+self.small_disjunct_instance_number)

        self.small_disjunct_imbalance_rate_accuracy = self.small_disjunct_class_accuracy*percentage_ir
        self.big_disjunct_imbalance_rate_accuracy = self.big_disjunct_class_accuracy * (1-percentage_ir)
        self.whole_imbalance_rate_accuracy = self.small_disjunct_imbalance_rate_accuracy + self.big_disjunct_imbalance_rate_accuracy
        output = output + "The big disjunct accuracy is :" + str(self.big_disjunct_class_accuracy)+ "\n"
        output = output + "The small disjunct accuracy is :" + str(self.small_disjunct_class_accuracy)+ "\n"
        output = output + "The whole_imbalance_rate_accuracy accuracy is :" + str(self.whole_imbalance_rate_accuracy)+ "\n"
        
        print("output: "+output)
        output_file.write(output)
        
if __name__ == "__main__":
        
        
        dataset_folder = 'A1'
        result_folder = 'results'
        algorithm_folder = 'c4.5'



        cwd = Path.cwd()

        file_train_name = cwd / dataset_folder / result_folder /algorithm_folder/  "result0.tra "
        file_test_name = cwd / dataset_folder / result_folder /algorithm_folder/  "result0.tst "
        
        sdiraf = SDIRAF()
        print("before call calculatSDIRAF")
        sdiraf.calculatSDIRAF(file_train_name)
        sdiraf.calculatSDIRAF(file_test_name)