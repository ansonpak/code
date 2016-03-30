s = str(input())
ss=s.split('#')
h=""
for i in reversed(ss):
    h=h+i+'#'
print(h[0:len(h)-1])