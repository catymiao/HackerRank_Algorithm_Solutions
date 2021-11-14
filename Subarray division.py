def birthday(s, d, m):
    # Write your code here
    ar=[]
    way_ct = 0
    for i in s:
        ar.append(i)
    for i in range(len(ar)):
        if sum(ar[i:i+m])==d:
            way_ct +=1
    return(way_ct)
                  
