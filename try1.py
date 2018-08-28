
class A(object):
    x = 10
    y = 20

    # def __init__(self, x=None, y=None):
    #     if x is not None:
    #         self.x = x
    #     if y is not None:
    #         self.y = y


if __name__ == '__main__':
    obj = A()

    print(obj.x, obj.y)

    obj1 = A()
    obj1.x = 1
    obj1.y = 2
    obj1.z = 3

    print(obj1.x, obj1.y, obj1.z)
    print(A.x, A.y)
    A.x = 1
    A.y = 2
    print(obj.x, obj.y)