def sherlockAndAnagrams(s):
    print(s[0:1])
    dict={}

    count=0

    for i in range(len(s)):

        for j in range(i+1,len(s)+1):

            # list1= list(s[i:j].strip())

            # list1.sort()

            # transf=''.join(list1)
            transf=s[i:j]
            # print(transf)

            if transf in dict: 
                dict[transf]=dict[transf]+1
            else: dict[transf]=1

    for i in range(len(s)):

        for j in range(i+1,len(s)+1):
            transf=s[i:j]
            if transf[::-1] in dict: 

                count+=dict[transf]

            
    # print(dict)     
    print(count)  

    return count   
    # dict={}
    # count=0
    # list1=[]
    # for i in range(len(s)):
    #     for j in range(i+1,len(s)+1):
    #         # list1= list(s[i:j].strip())
    #         # list1.sort()
    #         # transf=''.join(list1)

    #         # list1.append(object)

    #         transf=s[i:j]
    #         if transf in dict: 
    #             # count+=dict[transf]
    #             dict[transf]=dict[transf]+1
    #         else: dict[transf]=1  
    # for keys in dict.keys():
    #     if len(keys)==1:
    #         count+=dict[keys]-1
    #     else:
    #         if keys[::-1] in keys:
    #             count+=dict[keys]    

    # print(dict) 
    # print(count)
    # return count    
# s="kkkk"
# s="cdcd"
s="ifailuhkqq"
sherlockAndAnagrams(s)