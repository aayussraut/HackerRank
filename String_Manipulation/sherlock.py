def isValid(s):
    valid="NO"
    temp=[]
    dict_char={}
    for i in s:
        if i in dict_char:
            dict_char[i]+=1
        else:
            dict_char[i]=1
    print(dict_char)
    min_val=dict_char[s[0]]
    max_val=dict_char[s[0]]
    print(min_val)

    for value in dict_char.values():
        temp.append(value)

    max_val=max(temp)
    min_val=min(temp)
    if max_val==min_val:
        valid="YES"
    else:
        if (temp.count(max_val)==1 and max_val-min_val==1) or (temp.count(min_val)==1 and min_val==1 and temp[1]==max_val):
            valid="Yes"
    print(valid)

s="abcdefghhgfedecba"
isValid(s)