def bonAppetit(bill, k, b):
    ls_bill = []
    for i in bill:
        ls_bill.append(i)
    if b == (sum(ls_bill[:k]+ ls_bill[k+1:])//2):
        print('Bon Appetit') 
    else: 
        print(b-sum((ls_bill[:k]+ ls_bill[k+1:]))//2)
