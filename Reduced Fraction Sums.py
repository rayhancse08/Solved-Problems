def get_gcd(num1,num2):
    if num1 ==0:
        return num2
    return get_gcd(num2%num1,num1)

def eliminate_common_factor(numerator3,divisor3):
    common_factor = get_gcd(numerator3,divisor3)
    numerator3=numerator3 //common_factor
    divisor3=divisor3 //common_factor
    return numerator3,divisor3
    
    
def add_fraction(numerator1,divisor1,numerator2,divisor2):
    gcd = get_gcd(divisor1,divisor2)
    divisor3 = (divisor1 * divisor2) // gcd
    numerator3 = numerator1 * (divisor3 // divisor1) + numerator2 * (divisor3 // divisor2)
    numerator3,divisor3=eliminate_common_factor(numerator3,divisor3)
    return numerator3,divisor3
    
    

input_no=int(input("Input No: "))

result_list=[]
for i in range(input_no):
    input_string=input()
    eliminate_slash=input_string.replace('/'," ")
    eliminate_plus=eliminate_slash.replace('+'," ")
    convert_list=eliminate_plus.split(" ")
    
    numerator3,divisor3=add_fraction(int(convert_list[0]),int(convert_list[1]),int(convert_list[2]),int(convert_list[3]))
    result_str=str(numerator3)+"/"+str(divisor3)
    result_list.insert(i,result_str)
    


for item in result_list:
    print(item)
