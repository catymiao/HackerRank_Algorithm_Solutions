def diagonalDifference(arr):
    # Write your code here
    prim_sum = 0
    sec_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i ==j:
                prim_sum+=arr[i][j]
            if i+j == len(arr)-1:
                sec_sum += arr[i][j] 
    return(abs(prim_sum-sec_sum))

# be aware of the return position
