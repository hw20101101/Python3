class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello, world'
    
# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print("Complex 类的属性 r 为：", x.r)
print("Complex 类的属性 i 为：", x.i)