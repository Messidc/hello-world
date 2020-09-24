def gen():
    for x in ["a", "b", "c"]:
        yield x

for i in gen():
    print(i)