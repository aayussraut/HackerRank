# link: https://www.hackerrank.com/challenges/new-year-chaos/problem
def minimumBribes(q):
    bribe=0
    for i in range(len(q)-1,0,-1):
        if q[i]!=i+1:
            if q[i-1]==i+1:
                bribe+=1
                q[i-1],q[i]=q[i],q[i-1]
            elif q[i-2]==i+1:
                bribe+=2
                q[i-2],q[i-1],q[i]=q[i-1],q[i],q[i-2]
            else:
                print("Too chaotic")  
                return
    print(bribe)

q=[2,1,5,3,4]
minimumBribes(q)