def username_disparity(input_string,T):
    string_length=len(input_string)
    sum=0
    print("similarities are: ")
    for i in range(0,string_length,T):
        suffix=input_string[i:string_length]
        #print(suffix)
        count=0
        for j in range(0,len(suffix)):
            
            if suffix[j]==input_string[j]:
                       count+=1
            else:
                break
        print(count)
        sum+=count
    return sum
                
t_input=int(input("Enter T : "))
string=input("Enter String: ")
if string.islower():
    sum=username_disparity(string,t_input)
    print("Sum is ",sum)
else:
    print("Please input string  that contains only letters in the range ascii[a-z]")

