'''
推导式 + 函数式编程
学习列表推导式、匿名函数 lambda、高阶函数 map  filter
尝试用一行代码（推导式）生成 1 到 10 的平方数列表
尝试用 map 结合 lambda 给全班同学的名字加上统一前缀（例如将 ["张三", "李四"]
变为 ["QG_张三", "QG_李四"]）
'''

# 用一行代码（推导式）生成 1 到 10 的平方数列表
num_list=[i**2 for i in range(1,11)]
print(num_list)

# 用 map 结合 lambda 给全班同学的名字加上统一前缀
name_list=["张三", "李四"]
QG_name_list=list(map(lambda name_add:'QG'+name_add,name_list))
print(QG_name_list)

