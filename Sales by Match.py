import collections
def sockMerchant(n, ar):
    # Write your code here
    counter=collections.Counter(ar)
    ls = list()
    for key, value in dict(counter).items():
        ls.append(value)

    sales = []
    for i in ls:
        pair = i//2
        sales.append(pair)
    return(sum(sales)) 
