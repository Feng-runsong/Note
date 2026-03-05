'''
numpy
创建一个形状为 (3,4) 的二维数组，元素为 0-11 的连续整数
查看数组的 shape 、dtype 、ndim 属性
将数组变形为 (4,3)，并展平为一维数组
文档查阅：搜索 NumPy 官方文档「np.reshape」，确认 arr.reshape(4,-1) 是什么含义）
'''
import numpy as np

# 1. 创建一个形状为 (3,4) 的二维数组，元素为 0-11 的连续整数
arr = np.arange(0,12).reshape(3, 4)
print("原始数组：")
print(arr)

# 2. 查看数组的 shape、dtype、ndim 属性
print("数组属性：")
print("shape:", arr.shape)    # 输出: (3, 4)
print("dtype:", arr.dtype)    # 输出: int64（或int32，取决于系统）
print("ndim:", arr.ndim)      # 输出: 2

# 3. 将数组变形为 (4,3)
arr_reshaped = arr.reshape(4, 3)
print("变形为 (4,3) 的数组：")
print(arr_reshaped)

# 4. 展平为一维数组
arr_flattened = arr_reshaped.flatten()
print("展平后的一维数组：")
print(arr_flattened)

''''
根据 NumPy 官方文档，arr.reshape(4, -1) 的含义是：
第一个维度指定为 4：要求变形后的数组有 4 行
第二个维度设为 -1：这是一个特殊值，表示该维度的大小自动计算，使得数组元素总数保持不变
计算方式：
原数组元素总数 = 3 × 4 = 12 个元素
指定行数 = 4
自动计算的列数 = 总元素数 ÷ 指定行数 = 12 ÷ 4 = 3
所以 arr.reshape(4, -1) 等价于 arr.reshape(4, 3)。
官方文档说明：在 numpy.reshape 中，-1 表示该维度的大小由数组长度和其他维度推断得出，且只能有一个维度设置为 -1。
'''