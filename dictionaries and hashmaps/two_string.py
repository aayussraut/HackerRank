def twoStrings(s1, s2):
    dict_s1={}
    for i in s1:
        dict_s1.setdefault(i,0)
        dict_s1[i]+=1
    
    for i in s2:
        if i in dict_s1.keys():
            print("YES")
            return
    print("NO")
    return

# s1="be"
# s2="cat"
# s1="art"
# s2="and"
s1="hello"
s2="world"
twoStrings(s1, s2)