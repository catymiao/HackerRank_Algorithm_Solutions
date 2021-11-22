def utopianTree(n):
    # Write your code here
    height=[1]
    if n>=1:
        for i in range(1,n+1,1):
            if i%2==1:
                height.append(height[i-1]*2)
            if i%2==0:
                height.append(height[i-1]+1) 
    return(height[n])
