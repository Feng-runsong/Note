'''
基于 “封装 + 继承 + 多态” 设计「图形计算器」：
定义基类 Shape （私有属性 area ，封装计算面积的私有方法 calc_area ）
子类 Circle / Rectangle 继承 Shape ，重写面积计算逻辑（多态体现）
类变量记录所有图形的创建数量，实例变量存储各自尺寸
要求：通过实例调用公开方法获取面积，禁止直接访问私有属性
查 Python 官方文档：确认 str.strip() 的默认参数、隐含行为（比如是否仅删空格？）
总结一条结论，再写一段文档相关代码及运行结果
'''
class Shape:
    """图形基类，体现了封装的思想"""
    count = 0  # 类变量，记录所有图形的创建数量

    def __init__(self):
        # 将面积计算方法封装在内部，并在初始化时调用
        self.__area = self.__calc_area()
        Shape.count += 1  # 每创建一个实例，计数加1

    def __calc_area(self):
        """私有的面积计算方法，默认返回0，子类应重写此方法"""
        return 0

    def get_area(self):
        """公开的获取面积的接口，保护私有属性__area"""
        return self.__area


class Circle(Shape):
    """圆形类，继承自Shape"""
    def __init__(self, radius):
        self.radius = radius
        super().__init__()  # 调用父类初始化方法，保证计数和面积计算逻辑被触发

    def __calc_area(self):
        """重写父类的私有面积计算方法（多态的体现）"""
        import math
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    """矩形类，继承自Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__()

    def __calc_area(self):
        """重写父类的私有面积计算方法（多态的体现）"""
        return self.width * self.height


# 演示代码
if __name__ == "__main__":
    print("创建图形对象...")
    c1 = Circle(5)
    r1 = Rectangle(4, 6)
    c2 = Circle(3)

    print(f"圆 (半径=5) 的面积: {c1.get_area():.2f}")
    print(f"矩形 (4x6) 的面积: {r1.get_area()}")
    print(f"圆 (半径=3) 的面积: {c2.get_area():.2f}")

    print(f"总共创建的图形数量: {Shape.count}")

    # 下面的代码尝试直接访问私有属性，会报错，体现了封装性
    # print(c1.__area)  # AttributeError
    # print(c1.__calc_area())  # AttributeError

'''
str.strip() 方法官方文档查阅与结论:
str.strip() 方法在默认情况（不带参数）下，会移除字符串首尾的所有空白符，包括空格、制表符(\t)、换行符(\n)等，但不会移除字符串中间的
任何字符。当传入一个字符串作为参数时，它会把参数中的每个字符视为一个独立的集合，然后移除字符串首尾所有属于该集合的字符，直到遇到第一个
不在集合中的字符为止
'''