面向过程编程:

- 核心思想：把一个需求分解成一系列要执行的步骤，然后按照步骤依次执行这些任务(关注的是流程，步骤).
- 适用场景：面向过程编程非常直接，适合简单，线性的任务。

面向对象编程:

- 对象可以理解为现实中具体的人/物在程序中的数字化身(万物皆对象).
- 它把一个人/物的特征(属性)和功能(方法)打包到一起，是面向对象编程的基本单元。(关注的是谁来帮我做这件事儿)

---

类与对象

- 类：描述的是一组具有相同属性(特征)和方法(功能/行为)的模板。
- 对象：对象是类的实例，是基于类创建出来的(实例对象).


提示：对象是由类创建出来的，创建对象的过程，也称为对象的实例化。一个类可以创建无数个对象。

类

- 定义类的语法如下：

  ```python
  # 定义类	
  class 类名：	
  	pass
  
  #创建对象
  对象名=类名()	
  对象名。属性名1=属性值1	
  对象名，属性名2=属性值2
  
  # eg:
  # 定义类
  class Car:	
  	pass
  # 创建对象
  cl = Car()
  # 动态地为对象添加属性
  c1.brand ="BMW"	
  cl.name = "x5"	
  c1.price = 500000	
  print(cl.__dict__)
  ```



1. 说明：类名的命名规范，遵循大驼峰命名法，每个单词的首字母都是是大写，单词之间没有分隔符，比如：UserInfo,UserAccount.
2. 说明：__dict__是Python中用户自定义类实例的一个特殊属性，用于以字典形式存储对象的属性。

- 定义类时指定实例属性

```python
# 定义类
class 类名：
	def	__init__(self,参数列表):
		self.属性名 =	参数值	
		self.属性名 =	参数值

# 创建对象
对象名=类名(参数列表)

 # eg:
# 定义类
class Car:
	def __init__(self,c_brand,c_name,c_price):
        self.name = c_name	
        self.price = c_price
        
# 创建对象
c1 = Car("BMW","x5",500000)	
print(cl.__dict__)
```

1. self：方法的第一个参数，表示当前创建的实例对象
2. init__：初始化方法，对象创建后自动调用，主要用于设置对象的初始状态(设置对象属性)

说明：定义在类的外面的称之为函数，定义在类中的函数称之为方法

---

实例方法

- 在类中定义实例方法时，定义语法与之前学习的函数定义的方式是一致的。

  ```python
  # 定义类		
  class 类名：		
  	def __init__(self，形参列表):
  		self.属性名 =参数值
  		self.属性名=参数值	
  	def 方法名(self，形参列表):	
  		pass
  	def 方法名(self，形参列表):	
  		pass
  # 创建对象	
  对象名=类名(参数列表)		
  对象名.方法名(实参)
  
  # eg:
  #定义类	
  class Car:	
  	def __init__(self,brand,name,price):	
  		self.brand = brand	
  		self.nam = name	
  		self.price = price	
  	def running(self):	
  		print(f"{self.brand}{self.name}正在高速行驶...")
  	
      def total_cost(self, discount,rate):	
  		return self.price*discount+self.price * rate
  # 创建对象	
  c1 = Car("BMW","x5",500000)	
  total_cost = cl.total_cost(0.9, 0.1)	
  print(f"提车总价为：{total_price:.of}")	
  c1.running()
  ```

  说明:self表示当前实例对象，方法调用时无需传递

---

魔法方法
![1772286073860](C:\Users\123\AppData\Roaming\Typora\typora-user-images\1772286073860.png)

![1772286089503](C:\Users\123\AppData\Roaming\Typora\typora-user-images\1772286089503.png)

---

属性

![1772286182867](C:\Users\123\AppData\Roaming\Typora\typora-user-images\1772286182867.png)

---

异常(bug)

- 为什么要捕获异常:
  当程序运行出现异常，提供预案，处理异常，而不是让其中止程序运行

- 如何捕获异常，具体的语法:

  ```python
  try:
  	print("ABC".hello) 
  except NameError as e:
  	print("名称不存在，请检查，具体信息：",e)
  except ZeroDivisionError as e:
  	print("0不能做被除数，请检查，具体信息：",e) 
  except IndexError as e:
  	print("索引错误，请检查，具体信息：",e)
  except Exception as e:
  	print("其他错误，请检查，具体信息：",e) 
  finally:
  	print("无论正常执行还是出现异常，都要释放资源(~")
  ```

  

