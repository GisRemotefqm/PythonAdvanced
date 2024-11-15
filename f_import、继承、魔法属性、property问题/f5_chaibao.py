def test1(*args, **kwargs):
    print(args)
    print(kwargs)

def test2(*args, **kwargs):

    print(args)
    print(kwargs)
    test1(*args, **kwargs)


if __name__ == "__main__":

    test2(10, 20, 30, a=10, b=20)

