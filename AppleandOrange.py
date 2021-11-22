def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_position = []
    orange_position = []
    for i in range(len(apples)):
        apple_position.append(a + apples[i])
    for i in range(len(oranges)):
        orange_position.append(b+oranges[i])
    print(len([i for i in apple_position if i>=s and i<=t])) #list comprehension
    print(len([i for i in orange_position if i>=s and i<=t]))
