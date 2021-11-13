def breakingRecords(scores):
    ls_scores = []
    for i in scores: 
        ls_scores.append(i)
    break_low_ct = 0
    break_high_ct = 0
    for i in range(1,len(ls_scores),1):
        if ls_scores[i] > max(ls_scores[:i]):
             break_high_ct += 1
        if ls_scores[i] < min(ls_scores[:i]):
            break_low_ct += 1 
    return(break_high_ct,break_low_ct)
