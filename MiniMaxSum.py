def miniMaxSum(arr):
    # Write your code here
    min_sum=0
    max_sum=0
    arr.sort()
    for i in range(4):
        min_sum+=arr[i]
    for i in range(1,5,1):
        max_sum += arr[i]
    print(min_sum,max_sum)
