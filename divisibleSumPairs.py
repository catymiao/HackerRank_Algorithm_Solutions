def divisibleSumPairs(n, k, ar):
    # Write your code here
    ct = 0
    for i in range(n):
        for j in range(i+1,n,1):
            if (ar[i] + ar[j])% k == 0: 
                ct+=1
    return(ct)
                
