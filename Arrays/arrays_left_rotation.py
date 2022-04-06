from types import new_class


def rotLeft(a, d):
    arr=[x for x in range(1,a+1)]
    new_arr=[]
    new_arr=arr[d:]+arr[:d]
    print(new_arr)

a=5
d=4
rotLeft(a,d)