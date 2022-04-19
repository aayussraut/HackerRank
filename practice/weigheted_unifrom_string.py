def weightedUniformStrings(s, queries):
    dict={}
    list_val=[]
    for i in s:
        dict[i]=0
    for i in s:
        dict[i]+=(ord(i)-97+1)
        list_val.append(dict[i])
    list_val=set(list_val)
    print(list_val)

    for value in queries:
        if value in list_val:
            print("Yes")
        else:
            print("No")

s="abccddde"
queries=[6,1,3,12,5,9,10]
weightedUniformStrings(s, queries)
