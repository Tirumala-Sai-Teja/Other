def near(ar,n):
    dif=999
    ans=[]
    for i in ar:
        if abs(i-n)==dif:
            ans.append(i)
        elif abs(i-n)<dif:
            ans=[]
            ans.append(i)
            dif=abs(i-n)
    print(ans)
    return min(ans)
