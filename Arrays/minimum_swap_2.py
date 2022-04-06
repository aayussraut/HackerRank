from operator import indexOf


# def minimumSwaps(arr):
#     temp=sorted(arr)
#     swap=0
#     for i in range(len(arr)-1,0,-1):
#         if arr[i]==i+1:
#             continue
#         ind=indexOf(arr,i+1)
#         arr[i],arr[ind]=arr[ind],arr[i]
#         swap+=1
#         if temp==arr:
#             break
#     print(arr)
#     print(swap)

# --- works but time exceeded for 5 test case --- #

# def minimumSwaps(arr):
#     swap=0
#     for i in range(len(arr)):
#         if(arr[i]!=i+1):
#             j=i
#             while (arr[j]!=i+1):
#                 j+=1
#             arr[j],arr[i]=arr[i],arr[j]
#             swap+=1
#     print(arr)
#     print(swap)
def minimumSwaps(arr):
    swap=0
    i=0
    while (i<len(arr)):
        if(arr[i]!=i+1):
            temp=arr[i]
            arr[i]=arr[arr[i]-1]
            arr[temp-1]=temp
            swap+=1
        else:
            i+=1
    print(arr)
    print(swap)


# def minimumSwaps(arr):
#     # swap=True
#     # count=0
#     # for i in range(len(arr)-1):
#     #     if swap==True:
#     #         swap=False
#     #         for j in range(len(arr)-1-i):
#     #             if arr[i]>arr[j+1]:
#     #                 arr[i],arr[j+1]=arr[j+1],arr[i]
#     #                 swap=True
#     #                 count+=1

#     #     else:
#     #         break
#     # print(arr)
#     # print(count)


arr=[7,1,3,2,4,5,6]
minimumSwaps(arr)