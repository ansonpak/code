s = str(input())
ss=s.split(',')
y = int(ss[0])
m = int(ss[1])


if m==1:
    print(31)
elif m==3:
    print(31)
elif m==5:
    print(31)
elif m==7:
    print(31)
elif m==8:
    print(31)
elif m==10:
    print(31)
elif m==12:
    print(31)
elif m==4:
    print(30)
elif m==6:
    print(30)
elif m==9:
    print(30)
elif m==11:
    print(30)
elif m==2 and (y%4==0 and y%100!=0) or (y%400==0 and y%4000!= 0):
    print(29)
else:
    print(28)