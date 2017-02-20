# -*-coding:utf-8-*-

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

'''
__str__, __repr__
__repr__()返回的实例的代码表示，通常可以用它返回的字符串文本来重新创建这个实例
__str__()将实例转换为一个字符串，这也是由str()和print()函数所产生的输出
'''
