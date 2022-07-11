##this programme alows users to enter numbers between 10 and 20
from array import *
nums=array('i',[])
while len(nums)<5:
    num=int(input('enter number'))
    if num>=10 and num<=20:
        nums.append(num)
    else:
        print('outside range')
print('thank you') 
for i in nums:
     print(i)
        

