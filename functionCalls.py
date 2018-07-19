def a():
    print('a() was called.')
    b()
    c()
    print('a() is returning.')
    return

def b():
    print('b() was called.')
    c()
    print('b() is returning.')
    return

def c():
    print('c() was called.')
    print('c() is returning.')
    return

a()
