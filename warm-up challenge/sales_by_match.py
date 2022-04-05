#socks haru deko xa ..sock ko kati ota pair xa return garne
def sockMerchant(n, ar):
    total=0
    sock_dict={}
    for i in range(n):
        if ar[i] in sock_dict.keys():
            sock_dict[ar[i]]+=1
        else:
            sock_dict[ar[i]]=1
    
    for value in sock_dict.values():
        count=0
        count=value//2
        total+=count
    
    print(total)
        
# n=9
n=10
ar=[1 ,1, 3, 1 ,2 ,1 ,3 ,3 ,3, 3]
# ar=[10 ,20, 20 ,10, 10 ,30 ,50 ,10 ,20]
sockMerchant(n,ar)