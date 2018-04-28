import math
def check_power_of(x):
          for i in range(2,int(math.sqrt(x))+1):
                for j in range(2,int(math.sqrt(x))+1):
                       if pow(i,j)==x:
                         return 1
          return 0
     
def power(x):
     if x in [0,1]:
          return 1
     for i in range(2,int(math.sqrt(x))+1):
          
          for j in range(2,int(math.sqrt(x))+1):
               
               if pow(i,j)==x:
                    return 1
                    break
               
               if x-pow(i,j)==1:
                    return 1
                    break
               
               if x-pow(i,j)>4:
                    
                    remain_value = x-pow(i,j)
                    
                    is_power=check_power_of(remain_value)
                    
                    if is_power == 1:
                         return 1
                         break
     return 0

start_range=int(input("Start Range: "))
end_range=int(input("End Range: "))
count=0
for i in range(start_range,end_range+1):
     result=(power(i))
     if result == 1:
          count+=1

print(count)
