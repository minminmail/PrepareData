# -*- coding: utf-8 -*-

class MaxMin:
    
    # dataFile = open(r"C:\phd_algorithms\datasets_2021\A1\tra.dat","r")
    
    f1_max = -1
    f1_min =  100
    
    f2_max = -1
    f2_min =  100
    
    class_green_number = 0
    class_red_number = 0
    
    def __init__(self,dataFile):     
       self.dataFile = dataFile
   
    
    def get_max_min(self):
        
        #file = open("C:\phd_algorithms\datasets_2021\A1\tra.dat","r")
        dataFileOpen = open(self.dataFile,"r")
        lines = dataFileOpen.readlines()
        #print(lines)
    

        
        for line in lines:
           #print(line)
         if "@" not in line and "f1" not in line : 
                
               line_list = line.split(",")
               print(line_list)
               class_value = line_list[2]
               class_value = class_value.strip()
               print("class_value is ：" +class_value)
               if class_value ==  "green":
                    self.class_green_number=self.class_green_number + 1
               elif class_value == "red" :
                    self.class_red_number = self.class_red_number + 1
               else:
                 print("class_value is not green or red" )
        
               if line_list[0]!="f1":
        
                   f1_value = float(line_list[0])
                   if f1_value >self.f1_max:
                      self.f1_max = f1_value
                   if f1_value<self.f1_min:
                      self.f1_min = f1_value   
        
                   f2_value = float(line_list[1])    
                   if f2_value > self.f2_max:
                      self.f2_max = f2_value
                   if f2_value <self.f2_min:
                      self.f2_min = f2_value
         else:
                print("@ is in line :"+line)
                        
        print("f1_min is ：" +"%.3f" % (self.f1_min) )
        print("f1_max is ：" +"%.3f" %(self.f1_max))
        print("f2_min is ：" +"%.3f" %(self.f2_min))
        print("f2_max is ：" +"%.3f" %(self.f2_max))
        
        print("class_green_number is ：" +str(self.class_green_number))
        print("class_red_number is ：" +str(self.class_red_number))
        
        IR_value = int(self.class_green_number/self.class_red_number)
        print("IR_value is ：" +str(IR_value))
        
      
