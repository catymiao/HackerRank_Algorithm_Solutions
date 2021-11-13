def designerPdfViewer(h, word):
    # Write your code here
    ls_h = []
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    height_ls= []
    for i in h:
        ls_h.append(i)
    for i in word:
        for j in range(len(alpha)):
            if i==alpha[j]:
                height_ls.append(ls_h[j])
    return(max(height_ls)*len(word))
