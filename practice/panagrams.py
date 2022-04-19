def pangrams(s):
    s=s.replace(" ",'')
    s=s.lower()
    dict={}
    for i in s:
        dict[i]=0
    for i in s:
        dict[i]+=1
    # print(len(dict))
    # print(dict)
    if len(dict)==26:
        # print("panagram")
        return("panagram")
    # print("not panagram")
    return("not panagram")

s="We promptly judged antique ivory buckles for the next prize"
pangrams(s)
    