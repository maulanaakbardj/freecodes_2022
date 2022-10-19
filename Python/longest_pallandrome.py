s='cbbd'
def optimal(s):
    idx,lp=0,s[0]
    while idx<len(s):
        for idx_pred in (idx-2,idx-1):
            for i in range(len(s)-idx):
                if idx_pred<i or s[idx+i]!=s[idx_pred-i]:
                    break
                if (idx+i+1)-(idx_pred-i)>len(lp):
                    lp=s[idx_pred-i : idx+i+1]
                    print(lp,'gh',idx_pred,i,idx)
        idx+=1
    return lp

def app2(s):
    """
    middle-man approach
    """
    m,r='',''
    for i in range(len(s)):

        o=ck(s,i,i)
        e=ck(s,i,i+1)
        if len(o)>len(e):
            m=o
        else:
            m=e
        if len(m)>len(r):
            r=m
    return r

def ck(s,i,j):
    while 0<=i and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return s[i+1:j]

print(app2(s))