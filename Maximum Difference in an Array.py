def max_difference(input_list):
    list_length=len(input_list)
    max_diff=input_list[1]-input_list[0]
    
    for i in range(0,list_length):
             for j in range(i+1,list_length):
                  if input_list[j]-input_list[i]>max_diff:
                       max_diff=input_list[j]-input_list[i]
    return max_diff
    


n=int(input("How many element in arry :  "))
input_list=[]
print("Input array element")

for i in range(n):
    list_elements=int(input())
    input_list.insert(i,list_elements)

result=(max_difference(input_list))

print("Max difernece on array {0} is {1}".format(input_list,result))



    

