
def hourglassSum(arr):
    # maxi=0
    i=j=0
    maxi=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
    arr_len= len(arr) #for test case 3 and 7 
    # print(arr_len)
    for i in range(arr_len-2):
        for j in range(arr_len-2):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            maxi=max(sum,maxi)
    print(maxi)


arr=[
[1 ,1, 1 ,0 ,0 ,0],
[0, 1 ,0 ,0 ,0, 0],
[1 ,1 ,1 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0, 0, 0, 0],
[0, 0 ,0 ,0, 0, 0]]
hourglassSum(arr)