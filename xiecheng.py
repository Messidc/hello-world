#! -*- coding: utf-8 -*-
import inspect

# 协程使用生成器函数定义：定义体中有yield关键字。
def simple_coroutine():
    print('-> coroutine started')
    # yield 在表达式中使用；如果协程只需要从客户那里接收数据，yield关键字右边不需要加表达式（yield默认返回None）
    while True:
        x = yield
        print('-> coroutine received:', x)
    


my_coro = simple_coroutine()
print(my_coro) # 和创建生成器的方式一样，调用函数得到生成器对象。
# 协程处于 GEN_CREATED (等待开始状态)
print(inspect.getgeneratorstate(my_coro))

my_coro.send(None)
# 首先要调用next()函数，因为生成器还没有启动，没有在yield语句处暂停，所以开始无法发送数据
# 发送 None 可以达到相同的效果 my_coro.send(None) 
# next(my_coro)
# 此时协程处于 GEN_SUSPENDED (在yield表达式处暂停)
print(inspect.getgeneratorstate(my_coro))

# 调用这个方法后，协程定义体中的yield表达式会计算出42；现在协程会恢复，一直运行到下一个yield表达式，或者终止。
my_coro.send(42)
print(inspect.getgeneratorstate(my_coro))
my_coro.send(43)
print(inspect.getgeneratorstate(my_coro))
my_coro.send(44)
print(inspect.getgeneratorstate(my_coro))
my_coro.send(45)
print(inspect.getgeneratorstate(my_coro))