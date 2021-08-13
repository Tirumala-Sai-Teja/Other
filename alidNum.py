s=input()
st=s.split('-')
print(st)
if(len(st))!=3:
    print('Invalid Number Format')
else:
    if len(st[0])==3 and len(st[1])==3 and len(st[2])==4:
        print('Valid Number')
    else:
        print('Invalid Number Format')
