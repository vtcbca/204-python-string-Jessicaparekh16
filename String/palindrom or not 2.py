a=int(input("enter any string:"))
l=list(a.split ())
c=0
for i in l:
    b=l[c][::-1]
    if l[c]==b:
        print(l[c])
        c=c+1
    print("total() palindrom word is string()".format(c,1[c]))
