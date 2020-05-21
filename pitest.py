from functools import reduce
import itertools
import math
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
    natuals = itertools.count(1,2)
    ns = itertools.takewhile(lambda x:x<=2*N-1,natuals)  
    return reduce(lambda x,y:x+y , list(map(lambda x:(pow(-1,((x + 1) / 2 - 1)))*4/x, list(ns))))
    # return list(ns)
if __name__ == "__main__":
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
