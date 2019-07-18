a=40
b=0
space=40
while b<a-1 and a>0:
    print(' '*a+'*'+'*'*b)
    a-=1
    b+=2
for _ in range(4):
    print(' '*(space-1)+'|||')
print(' '*(space-5),'\_@_@_@_/')

####within a function()
def tree(a,b,space, n):
    while b<a-1 and a>0:
        print(' '*a+'*'+'*'*b)
        a-=1
        b+=2
    for _ in range(n):
        print(' '*(space-1)+'|||')
    print(' '*(space-5),'\_@_@_@_/')
a=40
b=0
space=40
n=4
tree(a,b,space, n)