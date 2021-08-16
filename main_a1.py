# -*- coding: utf-8 -*-

from draw import draw
class main_a1:
    
       if __name__ == "__main__":
        # print("Executing Algorithm.")

        # print("sys.argv: " + sys.argv[1])
        # execute(sys.argv[1])
        saveC1File="C:\phd_algorithms\datasets_2021\A1\data_green.dat"
        saveC2File="C:\phd_algorithms\datasets_2021\A1\data_red.dat"
        draw_data=draw(saveC1File,saveC2File)
        print("begin to paint in main")
        draw_data.paint()
        print("fnish to paint in main")