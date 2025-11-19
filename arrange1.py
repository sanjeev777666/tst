class Packages:
    def __init__(self):
      pass
     
    def sort(self,width, height, length, mass):
        vol1=width*height*length
        bulky_package,heavy_package=False,False
        if ((vol1>=float(1e+6))  or (length>=float(150) or height>=float(150) or width>=float(150))):
            bulky_package=True
        else:
            bulky_package=False
        if (mass>=float(20)):
            heavy_package=True
        else:
            heavy_package=False

        if(bulky_package and heavy_package):
            return "REJECTED"
        elif(bulky_package or heavy_package):
            return "SPECIAL"
        else:
            return "STANDARD"
if __name__=="__main__":
    obj1=Packages()
    print(obj1.sort(100,50,20,19))
        

