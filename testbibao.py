list=[]

for i in range(3):
    def makefunc(i):
        def func(x):
            return x*i
        return func
    list.append(makefunc(i))

for f in list:
    print(f(2))