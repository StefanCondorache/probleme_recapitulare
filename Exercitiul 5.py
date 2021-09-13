x,y=[],[]
for i in range(5):
    x.append(int(input('nr integer: ')))
print('a)',sum(x[0:3]))
y=x.copy()
print('b)',sum(y))
def prod(a):
    prod=1
    for i in a:
        prod*=i
    return prod
print('c)',prod(x)) 
print('d)',abs(y[2]))
print('e)',x[0]+y[0])