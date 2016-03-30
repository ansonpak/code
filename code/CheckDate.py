y = int(input())
m = int(input())
d = int(input())

if m==1:
    if d>31:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==2:
    if(y%4==0 and y%100!=0) or (y%400==0 and y%4000!= 0):
        if d>29:
            print("日期錯誤")
        else:
            print(str(y)+'/'+str(m)+'/'+str(d))
    else:
        if d>28:
            print("日期錯誤")
        else:
            print(str(y)+'/'+str(m)+'/'+str(d))
elif m==3:
    if d>31:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==4:
    if d>30:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==5:
    if d>31:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==6:
    if d>30:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==7:
    if d>31:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==8:
    if d>31:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==9:
    if d>30:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==10:
    if d>31:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==11:
    if d>30:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
elif m==12:
    if d>31:
        print("日期錯誤")
    else:
        print(str(y)+'/'+str(m)+'/'+str(d))
        