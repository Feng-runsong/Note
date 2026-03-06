'''
完成多元线性回归的类封装
代码实现解析解求解和梯度下降法求解
参考sklearn接口形式不允许调用机器学习库，仅可使用numpy
以波士顿房价数据集为例，划分训练集，测试集，并完成数据分析和预处理
完成模型训练并予以评价分析
'''
import numpy as np
import pandas as pd


class LinearRegression:
    """简单多元线性回归"""

    def __init__(self):
        self.coef = None  # 系数

    def fit(self, X, y):
        # 添加偏置项
        X = np.c_[np.ones(X.shape[0]), X]
        # 解析解求解
        self.coef = np.linalg.inv(X.T @ X) @ X.T @ y
        return self

    def predict(self, X):
        return X @ self.coef[1:] + self.coef[0]

    def r2_score(self, X, y):
        y_pred = self.predict(X)
        return 1 - np.sum((y - y_pred) ** 2) / np.sum((y - y.mean()) ** 2)


# 使用示例
print("=" * 50)
print("波士顿房价预测")
print("=" * 50)

# 加载数据
data = pd.read_csv('house_data.csv')
X = data.iloc[:, :-1].values  # 13个特征
y = data.iloc[:, -1].values  # 房价

# 标准化
X = (X - X.mean(axis=0)) / X.std(axis=0)

# 划分训练集和测试集
n_train = int(0.8 * len(X))
X_train, X_test = X[:n_train], X[n_train:]
y_train, y_test = y[:n_train], y[n_train:]

print(f"训练样本数: {len(X_train)}")
print(f"测试样本数: {len(X_test)}")
print(f"特征数: {X.shape[1]}")

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 评估
train_r2 = model.r2_score(X_train, y_train)
test_r2 = model.r2_score(X_test, y_test)

print(f"训练集 R²: {train_r2:.4f}")
print(f"测试集 R²: {test_r2:.4f}")

# 预测几个样本
y_pred = model.predict(X_test[:5])
print(f"前5个真实值: {y_test[:5].round(2)}")
print(f"前5个预测值: {y_pred.round(2)}")

# 系数大小（特征重要性）
coef_names = data.columns[:-1]
top_idx = np.argsort(np.abs(model.coef[1:]))[-3:][::-1]
print(f"最重要的3个特征:")
for idx in top_idx:
    print(f"  {coef_names[idx]}: {model.coef[idx + 1]:.4f}")