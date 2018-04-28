def approximate_matching(text_string,prefix_string,suffix_string):
    i,j=0,0
    max_prefix_count,max_suffix_count=0,0
    prefix_count,suffix_count=0,0
    sstr_start,sstr_end=0,0
    while i<len(data):
        start,end =-1,-1
        j,k=0,i
        prefix_count=0
        while (k<len(data) and j<len(prefix_string)) and (data[k] !=prefix_string[j]):
            j+=1
        while (k<len(data) and j<len(prefix_string)) and (data[k] ==prefix_string[j]):
                        if start==-1:
                            start=k
                        prefix_count+=1
                        k+=1
                        j+=1
        if prefix_count>max_prefix_count:
                      max_prefix_count=prefix_count
                      sstr_start=start

        k,j=i,0
        suffix_count=0
        while (k<len(data) and j<len(suffix_string)) and (data[k] !=suffix_string[j]):
            j+=1
        while (k<len(data) and j<len(suffix_string)) and (data[k] ==suffix_string[j]):
            suffix_count+=1
            k+=1
            j+=1
        end=k
        if suffix_count>max_suffix_count:
            max_suffix_count=suffix_count
            sstr_end=end
        i+=1
    if sstr_end>sstr_start:
        print(data[sstr_start:sstr_end])
    else:
        print(data[sstr_start-1])

data=input("String: ")
prefix_string=input("Prefix String: ")
suffix_string=input("Suffix String: ")
approximate_matching(data,prefix_string,suffix_string)


                
