def substrcount(n,s):
    count=0
    count+=n
    for i in range(0,n):
        start=i-1
        end=i+1
        #odd no palindrome
        while(start>=0 and end<n):
            if s[start]==s[end] and s[start]==s[i-1]:
                count+=1
                start-=1
                end+=1
            else:
                break
        #even no palindrome
        k=1
        while((i+k)<n and s[i+k]==s[i]):
            k+=1
        count+=k//2

    print(count)
# n=8
# s="mnonopoo"
# n=5
# s="asasd"
n=7
s="abcbaba"
# n=4
# s="aaaa"
substrcount(n, s)