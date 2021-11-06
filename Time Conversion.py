def timeConversion(s):
    ls = s.split(':')
    new_ls=[]
    if ls[0]=='12' and ls[2][2:]=='PM':
        return(s[:8])
    elif ls[0]=='12' and ls[2][2:]=='AM':
        return('00:'+s[3:8])
    elif ls[2][2:]=='PM':
        new_ls.append(str(int(ls[0])+12))
        new_ls.append(':')
        new_ls.append(ls[1])
        new_ls.append(':')
        new_ls.append(ls[2][:2])
        return(''.join(new_ls))
    else:
        return(s[:8])
