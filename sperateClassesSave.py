# -*- coding: utf-8 -*-
class seperateClassesSave:
    
    fromFile="C:\phd_algorithms\datasets_2021\A1\data.dat"
    saveC1File="C:\phd_algorithms\datasets_2021\A1\data_green.dat"
    saveC2File="C:\phd_algorithms\datasets_2021\A1\data_red.dat"
    
    def __init__(self,fromFile,saveC1File,saveC2File):
        self.fromFile = fromFile
        self.saveC1File = saveC1File
        self.saveC2File = saveC2File
    
    def save_classes_files(self):
        
        file = open(self.fromFile,"r")
        #file = open("C:\phd_algorithms\datasets_2021\A1\tra.dat","r")
        lines = file.readlines()
        #print(lines)

        class_green_number = 0
        class_red_number = 0
        string_green= ""
        string_red =  ""
        
        for line in lines:
           #print(line)
         if "@" not in line and "f1" not in line : 
                
               line_list = line.split(",")
               print(line_list)
               class_value = line_list[2]
               class_value = class_value.strip()
               print("class_value is ：" +class_value)
               if class_value ==  "green":
                    class_green_number=class_green_number + 1
                    string_green= string_green + line + "\n"
               elif class_value == "red" :
                    class_red_number = class_red_number + 1
                    string_red= string_red + line + "\n"
               else:
                 print("class_value is not green or red" )
        
           
         else:
                print("@ is in line :"+line)
        
        file = open(self.saveC1File,"ab")               
        bytes_data = bytes(string_green, 'utf-8')
        file.write(bytes_data)
        
        file = open(self.saveC2File,"ab")               
        bytes_data = bytes(string_red, 'utf-8')
        file.write(bytes_data)
        
        print(string_red)