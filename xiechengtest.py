import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(2)
    print('Hello again! (%s)' % threading.currentThread())

@asyncio.coroutine
def fuck():
    print('Fuck world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(5)
    print('Fuck again! (%s)' % threading.currentThread())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [fuck(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

