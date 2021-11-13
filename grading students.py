def gradingStudents(grades):
    newgrades=[]
    for i in grades: 
        if i >= 38 and (i//5+1)*5 - i <3:
            newgrades.append((i//5+1)*5)
        else:
            newgrades.append(i)

    return(newgrades)
