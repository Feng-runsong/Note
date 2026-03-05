'''
能源核心数据清洗处理
数据：raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99",
"120"]。（可以自己设计数据）
实现自动跳过非数字项、仅保留≥80 数值、归一化为 0.xx-1.xx 小数，且根据结果是否 < 1.0
对应报「核心过载」或输出「运转正常」
思考题：是先清洗再过滤，还是先过滤再清洗？如何利用 try-except 配合函数式编程？
'''
def clean_data (raw_data):
    '''
    能源核心数据清洗处理
    :param raw_data:待处理数据
    '''
    for data in raw_data:
        # 清洗数据
        try:
            num = float(data)
            # 过滤数据
            if 80.0<=num<=200:
                # 归一化处理
                normalized = (num - 80.0) / (200.0- 80.0)
                if normalized < 1.0:
                    print('结果为:',normalized)
                    print('运转正常,处理结果<1')
                else:
                    print('结果为:',normalized)
                    print('核心过载,处理结果>1')
            elif num<80:
                print('核心过载,该数据小于80,太小!')
            else:
                print('核心过载,该数据大于200,太大!')

        # 跳过非数字项
        except Exception:
                print('核心过载,该数据不是数字')
        continue

# 创建一组数据
raw_data = []
i=1
while i<=5:
    a=input('请输入一小句话或一个0~200之间的数:')
    raw_data.append(a)
    i=i+1

print(raw_data)

# 调用函数
clean_data(raw_data)

'''
思考题:
先清洗再过滤
原因:非数字项无法进行数值比较,先清洗可以统一数据类型,避免类型错误异常
'''