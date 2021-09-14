temp=[]
for i in range(24):
    temp.append(int(input('temperatura: ')))
print('a)', sum(temp)/24)
print('b)','maximul:',max(temp),'\n','  minimul:',min(temp))
if temp.count(max(temp))>1:
    print('c) maximele')
    lmax,temp1=[],temp.copy()
    for i in temp1:
        if i==max(temp):
            lmax.append(temp1.index(i))
            temp1[temp1.index(i)]=(sum(temp1)/24)
    for i in lmax:
        print('Orele:',i+1)
else: print('c)',temp.index(max(temp))+1)
if temp.count(min(temp))>1:
    print('d) minimele')
    lmin,temp1=[],temp.copy()
    for i in temp1:
        if i==min(temp):
            lmin.append(temp1.index(i))
            temp1[temp1.index(i)]=(sum(temp1)//24)
    for i in lmin:
        print('Orele:',i+1)
else: print('d)',temp.index(min(temp))+1)
