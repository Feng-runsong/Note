'''
泰坦尼克号数据集可视化
分别设计对各指标的生还数（率）进行对比可视化
分析可视化结果
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置为英文显示
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('titanic_train.csv')

# 设置可视化风格
sns.set_style('whitegrid')
sns.set_palette('Set2')

# 创建子图布局
fig = plt.figure(figsize=(20, 24))

# 1. 性别与生还关系
ax1 = fig.add_subplot(4, 3, 1)
sex_survived = df.groupby('Sex')['Survived'].agg(['count', 'sum', 'mean'])
sex_survived['mean'] = sex_survived['mean'] * 100
sex_labels = ['Female', 'Male']
ax1.bar(sex_labels, sex_survived['mean'], color=['#ff9999', '#66b3ff'])
ax1.set_title('Survival Rate by Sex', fontsize=14, fontweight='bold')
ax1.set_xlabel('Sex')
ax1.set_ylabel('Survival Rate (%)')
for i, v in enumerate(sex_survived['mean']):
    ax1.text(i, v + 1, f'{v:.1f}%', ha='center', fontsize=11)

# 2. 客舱等级与生还关系
ax2 = fig.add_subplot(4, 3, 2)
class_survived = df.groupby('Pclass')['Survived'].agg(['count', 'sum', 'mean'])
class_survived['mean'] = class_survived['mean'] * 100
class_labels = ['1st Class', '2nd Class', '3rd Class']
ax2.bar(class_labels, class_survived['mean'], color=['#ffd700', '#c0c0c0', '#cd7f32'])
ax2.set_title('Survival Rate by Passenger Class', fontsize=14, fontweight='bold')
ax2.set_xlabel('Passenger Class')
ax2.set_ylabel('Survival Rate (%)')
for i, v in enumerate(class_survived['mean']):
    ax2.text(i, v + 1, f'{v:.1f}%', ha='center', fontsize=11)

# 3. 年龄分布与生还关系
ax3 = fig.add_subplot(4, 3, 3)
bins = [0, 5, 12, 18, 35, 50, 65, 100]
labels = ['0-5', '6-12', '13-18', '19-35', '36-50', '51-65', '65+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
age_survived = df.groupby('AgeGroup', observed=True)['Survived'].mean() * 100
ax3.plot(age_survived.index, age_survived.values, marker='o', linewidth=2, markersize=8, color='green')
ax3.set_title('Survival Rate by Age Group', fontsize=14, fontweight='bold')
ax3.set_xlabel('Age Group')
ax3.set_ylabel('Survival Rate (%)')
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)

# 4. 家庭规模与生还关系
ax4 = fig.add_subplot(4, 3, 4)
df['FamilySize'] = df['Siblings/Spouses Aboard'] + df['Parents/Children Aboard'] + 1
family_survived = df.groupby('FamilySize')['Survived'].agg(['count', 'mean'])
family_survived['mean'] = family_survived['mean'] * 100
ax4.bar(family_survived.index, family_survived['mean'], color='orange')
ax4.set_title('Survival Rate by Family Size', fontsize=14, fontweight='bold')
ax4.set_xlabel('Family Size')
ax4.set_ylabel('Survival Rate (%)')
for i, v in enumerate(family_survived['mean']):
    if not np.isnan(v):
        ax4.text(family_survived.index[i], v + 1, f'{v:.1f}%', ha='center', fontsize=9)

# 5. 票价分段与生还关系
ax5 = fig.add_subplot(4, 3, 5)
fare_bins = [0, 10, 25, 50, 100, 600]
fare_labels = ['0-10', '10-25', '25-50', '50-100', '100+']
df['FareGroup'] = pd.cut(df['Fare'], bins=fare_bins, labels=fare_labels)
fare_survived = df.groupby('FareGroup', observed=True)['Survived'].mean() * 100
ax5.bar(fare_labels, fare_survived.values, color='purple')
ax5.set_title('Survival Rate by Fare', fontsize=14, fontweight='bold')
ax5.set_xlabel('Fare Range')
ax5.set_ylabel('Survival Rate (%)')
for i, v in enumerate(fare_survived.values):
    ax5.text(i, v + 1, f'{v:.1f}%', ha='center', fontsize=10)

# 6. 兄弟姐妹/配偶数量与生还关系
ax6 = fig.add_subplot(4, 3, 6)
sibsp_survived = df.groupby('Siblings/Spouses Aboard')['Survived'].mean() * 100
ax6.bar(sibsp_survived.index, sibsp_survived.values, color='coral')
ax6.set_title('Survival Rate by Siblings/Spouses', fontsize=14, fontweight='bold')
ax6.set_xlabel('Siblings/Spouses')
ax6.set_ylabel('Survival Rate (%)')
for i, v in enumerate(sibsp_survived.values):
    ax6.text(sibsp_survived.index[i], v + 1, f'{v:.1f}%', ha='center', fontsize=10)

# 7. 父母/子女数量与生还关系
ax7 = fig.add_subplot(4, 3, 7)
parch_survived = df.groupby('Parents/Children Aboard')['Survived'].mean() * 100
ax7.bar(parch_survived.index, parch_survived.values, color='teal')
ax7.set_title('Survival Rate by Parents/Children', fontsize=14, fontweight='bold')
ax7.set_xlabel('Parents/Children')
ax7.set_ylabel('Survival Rate (%)')
for i, v in enumerate(parch_survived.values):
    ax7.text(parch_survived.index[i], v + 1, f'{v:.1f}%', ha='center', fontsize=10)

# 8. 性别+客舱等级交叉分析
ax8 = fig.add_subplot(4, 3, 8)
pivot_sex_class = df.pivot_table(values='Survived', index='Pclass', columns='Sex', aggfunc='mean') * 100
pivot_sex_class.columns = ['Female', 'Male']
pivot_sex_class.index = ['1st Class', '2nd Class', '3rd Class']
pivot_sex_class.plot(kind='bar', ax=ax8, color=['#ff9999', '#66b3ff'])
ax8.set_title('Survival Rate: Sex × Class', fontsize=14, fontweight='bold')
ax8.set_xlabel('Passenger Class')
ax8.set_ylabel('Survival Rate (%)')
ax8.legend(title='Sex')
ax8.set_xticklabels(pivot_sex_class.index, rotation=0)
for container in ax8.containers:
    ax8.bar_label(container, fmt='%.1f%%', padding=3, fontsize=9)

# 9. 总体生还比例
ax9 = fig.add_subplot(4, 3, 9)
survived_count = df['Survived'].value_counts()
labels = ['Deceased', 'Survived']
ax9.pie(survived_count.values, labels=labels, autopct='%1.1f%%',
        colors=['#ff6b6b', '#51cf66'], explode=(0.05, 0), startangle=90)
ax9.set_title('Overall Survival Proportion', fontsize=14, fontweight='bold')

# 10. 性别生还人数对比
ax10 = fig.add_subplot(4, 3, 10)
sex_survived_count = df.groupby(['Sex', 'Survived']).size().unstack()
sex_survived_count.columns = ['Deceased', 'Survived']
sex_survived_count.index = ['Female', 'Male']
sex_survived_count.plot(kind='bar', ax=ax10, color=['#ff6b6b', '#51cf66'])
ax10.set_title('Survival Count by Sex', fontsize=14, fontweight='bold')
ax10.set_xlabel('Sex')
ax10.set_ylabel('Count')
ax10.legend(title='Status')
ax10.set_xticklabels(sex_survived_count.index, rotation=0)
for container in ax10.containers:
    ax10.bar_label(container, padding=3, fontsize=9)

# 11. 客舱等级生还人数对比
ax11 = fig.add_subplot(4, 3, 11)
class_survived_count = df.groupby(['Pclass', 'Survived']).size().unstack()
class_survived_count.columns = ['Deceased', 'Survived']
class_survived_count.index = ['1st Class', '2nd Class', '3rd Class']
class_survived_count.plot(kind='bar', ax=ax11, color=['#ff6b6b', '#51cf66'])
ax11.set_title('Survival Count by Class', fontsize=14, fontweight='bold')
ax11.set_xlabel('Passenger Class')
ax11.set_ylabel('Count')
ax11.legend(title='Status')
ax11.set_xticklabels(class_survived_count.index, rotation=0)
for container in ax11.containers:
    ax11.bar_label(container, padding=3, fontsize=9)

# 12. 年龄段生还人数对比
ax12 = fig.add_subplot(4, 3, 12)
age_survived_count = df.groupby(['AgeGroup', 'Survived'], observed=True).size().unstack()
age_survived_count.columns = ['Deceased', 'Survived']
age_survived_count.plot(kind='bar', ax=ax12, color=['#ff6b6b', '#51cf66'])
ax12.set_title('Survival Count by Age Group', fontsize=14, fontweight='bold')
ax12.set_xlabel('Age Group')
ax12.set_ylabel('Count')
ax12.legend(title='Status')
plt.setp(ax12.xaxis.get_majorticklabels(), rotation=45)
for container in ax12.containers:
    ax12.bar_label(container, padding=2, fontsize=8)

plt.tight_layout()
plt.savefig('titanic_survival_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print('可视化完成~')

