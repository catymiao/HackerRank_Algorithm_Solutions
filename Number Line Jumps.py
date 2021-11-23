def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 == v2:
        return('NO')
    elif (x2-x1)/(v1-v2)>0 and ((x2-x1)/(v1-v2)).is_integer()==True:
        return('YES')
    else:
        return('NO')
