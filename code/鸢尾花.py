'''
完成K-means的类封装
参考sklearn接口形式不允许调用机器学习库，仅可使用numpy 以鸢尾花数据集为例，完成
模型训练并予以评价分析结果
'''
import numpy as np
import random

class KMeans:
    def __init__(self, n_clusters=3, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centers = None
        self.labels = None

    def fit(self, X):
        # 随机初始化中心点
        idx = random.sample(range(len(X)), self.n_clusters)
        self.centers = X[idx].copy()

        for _ in range(self.max_iter):
            # 分配标签
            distances = np.zeros((len(X), self.n_clusters))
            for i, center in enumerate(self.centers):
                distances[:, i] = np.sum((X - center) ** 2, axis=1)
            new_labels = np.argmin(distances, axis=1)

            # 检查收敛
            if hasattr(self, 'labels') and np.array_equal(self.labels, new_labels):
                break
            self.labels = new_labels

            # 更新中心点
            for i in range(self.n_clusters):
                if np.sum(self.labels == i) > 0:
                    self.centers[i] = np.mean(X[self.labels == i], axis=0)

        return self

    def predict(self, X):
        distances = np.zeros((len(X), self.n_clusters))
        for i, center in enumerate(self.centers):
            distances[:, i] = np.sum((X - center) ** 2, axis=1)
        return np.argmin(distances, axis=1)


# 加载数据
data = []
true_labels = []
with open('Iris.csv', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        data.append([float(x) for x in parts[:4]])
        true_labels.append(parts[4])

X = np.array(data)
species = list(set(true_labels))
y_true = np.array([species.index(l) for l in true_labels])

# 训练模型
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_pred = kmeans.predict(X)

# 简单评估
print("聚类结果分析")
print("=" * 30)

# 1. 各簇大小
print("各簇样本数:")
for i in range(3):
    print(f"簇{i}: {np.sum(y_pred == i)}个")

# 2. 准确率（按最佳匹配）
correct = 0
for i in range(3):
    cluster_mask = (y_pred == i)
    if np.sum(cluster_mask) > 0:
        true_in_cluster = y_true[cluster_mask]
        most_common = np.bincount(true_in_cluster).argmax()
        correct += np.sum(true_in_cluster == most_common)

accuracy = correct / len(y_true)
print(f"准确率: {accuracy:.2%}")

# 3. 各类别分布
print("各类别在簇中的分布:")
print("类别\t簇0\t簇1\t簇2")
for i in range(3):
    counts = []
    for j in range(3):
        counts.append(np.sum((y_true == i) & (y_pred == j)))
    print(f"类{i}\t{counts[0]}\t{counts[1]}\t{counts[2]}")