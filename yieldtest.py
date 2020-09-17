def num():
    a = yield 1
    while True:
        a = yield a



if __name__ == "__main__":
    c = num()
    s=c.send(None)
    s=c.send(5)
    s=c.send(50)

    


