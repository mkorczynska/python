s=1
e=500
for i in range(s, e):
    i=str(i)
    p=1
    for j in i:
        j=int(j)
        if j%2==0:
            p=0
            break
    if p==1:
        print(i)
