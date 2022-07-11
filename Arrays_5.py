from array import *
import random
arrray_1=array('i',[])
for a in range(0,3):
    arrray=int(input('enter 3 numbers'))
    arrray_1.append(arrray)
arrray_2=array('i',[])
for b in range(0,5):
    arrray=random.randint(100,1000)
    arrray_2.append(arrray)
arrray_1.extend(arrray_2)
print(arrray_1)  
print(arrray_1)  
for i in arrray_1:
    print(i) 




