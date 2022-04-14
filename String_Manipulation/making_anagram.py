def makeAnagram(a, b):
    sum=0
    dict_ana={}
  
    for x in a:
        if x in dict_ana:
            dict_ana[x]+=1
        else:
            dict_ana[x]=1
    for x in b:
        if x in dict_ana:
            dict_ana[x]-=1
        else:
            dict_ana[x]=-1
    print(dict_ana)

    for value in dict_ana.values():
        sum+=abs(value)
    print(sum)
            


                

a= "fcrxzwscanmligyxyvym"

b="jxwtrhvujlmrpdoqbisbwhmgpmeoke"
makeAnagram(a,b)