import array


def arrayManipulation(n, queries):
    array=[0 for x in range(0,n+1)]
    
    for a,b,k in queries:
        array[a-1]+=k
        array[b]-=k
    tmp=0
    maxi=0
    for i in array:
        tmp+=i
        maxi=max(maxi,tmp)
    print (maxi)


queries=[[1 ,2, 100],
[2, 5 ,100],
[3 ,4 ,100]]
n=5
arrayManipulation(n,queries)