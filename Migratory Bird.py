import collections

def migratoryBirds(arr):
    # Write your code here
    counter=collections.Counter(arr)
    max_key = max(dict(counter).items(), key=lambda x: x[1])
    listOfKeys = list()
    for key, value in dict(counter).items():
        if value == max_key[1]:
            listOfKeys.append(key)
    return(min(listOfKeys))
