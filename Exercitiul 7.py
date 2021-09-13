venit_zi=[]
for i in range(7):
    x=int(input("venitul zilnic: "))
    venit_zi.append(x)
print('a)',sum(venit_zi))
print('b)',sum(venit_zi)/7)
zile=['Luni','Marți','Miercuri','Joi','Vineri','Sâmbătă','Duminică']
print('c)',zile[venit_zi.index(max(venit_zi))])
print('d)',zile[venit_zi.index(min(venit_zi))])