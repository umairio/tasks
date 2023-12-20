# yeild

def fungen(n):
    for i in range(n,0,-1):
       yield i
       

x=fungen(5)
print (next(x))
print (next(x))
print (next(x))

def genfun():
    for i in range(10,0,-1):
        yield i

a=list(map(lambda x:print(x), genfun()))