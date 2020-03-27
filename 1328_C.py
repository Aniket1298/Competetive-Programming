for _ in range(input()):
    n=input()
    s=raw_input()
    a=''
    b=''
    flag=0
    for i in range(n):
        if flag==0:
            if s[i]=='2':
                a+='1'
                b+='1'
            elif s[i]=='0':
                a+='0'
                b+='0'
            else:
                a+='1'
                b+='0'
                flag=1
        else:
            a+='0'
            b+=s[i]
    print a
    print b
