'''
pandas
处理 CSV 数据，以加州房价为例，使用pandas处理
加州房价数据集
matplotlib
配合 Matplotlib 画图，用 NumPy 生成 x 轴数据，绘制正弦曲线
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 读取数据 - 使用正确的编码和参数
try:
    # 尝试不同的读取方式
    df = pd.read_csv('加州房价数据集.csv', encoding='utf-8')
except:
    try:
        df = pd.read_csv('加州房价数据集.csv', encoding='gbk')
    except:
        # 如果还是不行，手动处理数据
        print("使用备用方法读取数据...")
        with open('加州房价数据集.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 提取有效数据行
        data_lines = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('经度') and not line.startswith('longitude'):
                # 替换中文逗号和空格
                line = line.replace('，', ',').replace(' ', '')
                data_lines.append(line)

        # 创建DataFrame
        data = []
        for line in data_lines[:100]:  # 取前100行数据
            parts = line.split(',')
            if len(parts) >= 10:  # 确保有足够的数据列
                try:
                    row = [
                        float(parts[0]), float(parts[1]), float(parts[2]),
                        float(parts[3]), float(parts[4]), float(parts[5]),
                        float(parts[6]), float(parts[7]), float(parts[8]),
                        parts[9] if len(parts) > 9 else 'UNKNOWN'
                    ]
                    data.append(row)
                except:
                    continue

        df = pd.DataFrame(data, columns=[
            'longitude', 'latitude', 'housing_median_age', 'total_rooms',
            'total_bedrooms', 'population', 'households', 'median_income',
            'median_house_value', 'ocean_proximity'
        ])

# 2. 数据预处理
print("原始数据形状:", df.shape)
print("前几行数据:")
print(df.head())

# 转换数据类型
df['median_income'] = pd.to_numeric(df['median_income'], errors='coerce')
df['median_house_value'] = pd.to_numeric(df['median_house_value'], errors='coerce')
df['population'] = pd.to_numeric(df['population'], errors='coerce')
df['housing_median_age'] = pd.to_numeric(df['housing_median_age'], errors='coerce')
df['total_rooms'] = pd.to_numeric(df['total_rooms'], errors='coerce')

# 删除缺失值
df = df.dropna()

print(f"清洗后数据形状: {df.shape}")
print(f"数据类型:{df.dtypes}")

# 3. 创建第一个图表--使用numpy拟合人口与房价关系

# 获取数据并过滤异常值
x = df['population'].values
y = df['median_house_value'].values

# 只取人口小于5000的数据点
mask = (x < 5000) & (x > 0)
x_filtered = x[mask]
y_filtered = y[mask]

plt.scatter(x_filtered, y_filtered, label='原始数据')

# 使用numpy进行多项式拟合
if len(x_filtered) > 10:  # 确保有足够的数据点
    z = np.polyfit(x_filtered, y_filtered, 2)
    p = np.poly1d(z)

    # 生成平滑的x轴数据用于绘制拟合曲线
    x_smooth = np.linspace(x_filtered.min(), x_filtered.max(), 100)
    plt.plot(x_smooth, p(x_smooth), 'r-', linewidth=2, label='拟合曲线')
    plt.xlabel('人口数量')
    plt.ylabel('房价中位数')
    plt.title('人口与房价关系（带拟合曲线）')
    plt.show()

# 4. 创建第二个图表--不同收入区间的平均房价趋势
plt.figure(figsize=(14, 6))
# 统计每个地理位置的数据量
location_counts = df['ocean_proximity'].value_counts()
print(f"地理位置分布:{location_counts}")

# 只保留数据量足够的位置
valid_locations = location_counts[location_counts > 5].index.tolist()
df_location = df[df['ocean_proximity'].isin(valid_locations)]

#  收入分组与平均房价趋势

# 按收入分组
income_bins = np.linspace(df['median_income'].min(), df['median_income'].max(), 15)
df['income_group'] = pd.cut(df['median_income'], bins=income_bins)

# 计算每组平均房价
group_stats = df.groupby('income_group')['median_house_value'].agg(['mean', 'count'])
group_stats = group_stats[group_stats['count'] > 5]  # 过滤数据量少的组

# 获取每组的中点作为x轴数据
group_centers = [(interval.left + interval.right) / 2 for interval in group_stats.index]
x_positions = np.array(group_centers)
y_values = group_stats['mean'].values

# 绘制散点和趋势线
plt.scatter(x_positions, y_values, s=50, alpha=0.7, label='平均房价')

# 使用numpy生成平滑曲线
if len(x_positions) > 3:
    x_smooth = np.linspace(x_positions.min(), x_positions.max(), 100)

    # 使用插值
    from scipy import interpolate

    f = interpolate.interp1d(x_positions, y_values, kind='cubic', fill_value='extrapolate')
    y_smooth = f(x_smooth)

    plt.plot(x_smooth, y_smooth, 'r-', linewidth=2, label='趋势线')

plt.xlabel('收入区间')
plt.ylabel('平均房价')
plt.title('不同收入区间的平均房价趋势')
plt.suptitle('加州房价深入分析', fontsize=16, y=1.02)
plt.show()

# 5. 创建第三个图表--不同地理位置房价分布密度
plt.figure(figsize=(12, 6))

# 使用numpy创建x轴数据
x_density = np.linspace(df['median_house_value'].min(),
                        df['median_house_value'].max(), 200)

# 为不同地理位置绘制房价密度曲线
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i, location in enumerate(valid_locations[:5]):  # 只画前5个
    location_data = df[df['ocean_proximity'] == location]['median_house_value'].values

    if len(location_data) > 10:
        # 简单的核密度估计
        from scipy import stats

        kernel = stats.gaussian_kde(location_data)
        density = kernel(x_density)

        plt.plot(x_density, density, color=colors[i % len(colors)],
                 linewidth=2, label=location)

plt.xlabel('房价中位数')
plt.ylabel('密度')
plt.title('不同地理位置房价分布密度曲线')
plt.show()

print("数据分析完成！")
print(f"最终数据统计：")
print(f"总记录数: {len(df)}")
print(f"房价范围: {df['median_house_value'].min():.0f} - {df['median_house_value'].max():.0f}")
print(f"平均房价: {df['median_house_value'].mean():.0f}")
print(f"中位收入范围: {df['median_income'].min():.2f} - {df['median_income'].max():.2f}")