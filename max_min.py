# -*- coding: utf-8 -*-

file = open(r"C:\phd_algorithms\datasets_2021\A1\data.dat","r")
#file = open("C:\phd_algorithms\datasets_2021\A1\tra.dat","r")
lines = file.readlines()
#print(lines)
f1_max = -1
f1_min =  100

f2_max = -1
f2_min =  100
class_green_number = 0
class_red_number = 0

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
       elif class_value == "red" :
            class_red_number = class_red_number + 1
       else:
         print("class_value is not green or red" )

       if line_list[0]!="f1":

           f1_value = float(line_list[0])
           if f1_value >f1_max:
              f1_max = f1_value
           if f1_value<f1_min:
              f1_min = f1_value   

           f2_value = float(line_list[1])    
           if f2_value > f2_max:
              f2_max = f2_value
           if f2_value <f2_min:
              f2_min = f2_value
 else:
        print("@ is in line :"+line)
                
print("f1_min is ：" +str(f1_min))
print("f1_max is ：" +str(f1_max))
print("f2_min is ：" +str(f2_min))
print("f2_max is ：" +str(f2_max))

print("class_green_number is ：" +str(class_green_number))
print("class_red_number is ：" +str(class_red_number))

IR_value = int(class_green_number/class_red_number)
print("IR_value is ：" +str(IR_value))