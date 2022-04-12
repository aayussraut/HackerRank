def checkMagazine(magazine, note):
    magazine_dict={}
    for i in magazine:
        magazine_dict.setdefault(i,0)
        magazine_dict[i]+=1
    print(magazine_dict)
    for i in note:
        if i in magazine_dict and magazine_dict[i]==0:
            print("No")
            return
        magazine_dict[i]-=1
    print("Yes")
    return
    # magazine_arr=magazine.split()
    # note_arr=note.split()
    # for i in note_arr:
    #     if i in magazine_arr:
    #         magazine_arr.remove(i)
    #     else:
    #         print("NO")
    #         return
    # print("YES")
    # return
    # print(magazine_arr)
magazine=['two','times','three','is','not', 'four']
note=["two" ,"times" ,"two" ,"is", "four"]
checkMagazine(magazine, note)