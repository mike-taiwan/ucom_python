def foo(x, y):
    return "[foo]:result=%s" % str(x + y)


def bar(x, y):
    return "[bar]:result=%s" % str(x * y)


if __name__ == '__main__':
    print foo(1, 2)
    print bar(3, 4)
