def jumpingOnClouds(c):
    count=0
    i=0
    while(i<len(c)-2):
        if(c[i+2]==0):
            i+=2
        else:
            i+=1
        count+=1
    print(count)

c=[0 ,0, 0 ,0 ,1 ,0]
jumpingOnClouds(c)