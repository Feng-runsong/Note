'''
情报解密
截获一条杂乱情报：" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;
Mission:2025-RESCUE-X "
请运用所有所学知识清洗数据：利用 String 方法去除干扰空格；利用 Set 帮特工去除重复装
备；利用 Slicing 截取核心任务代号；利用 Tuple锁定坐标；最后将所有信息归档进一个 Dict
档案中
'''

raw_info=" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;Mission:2025-RESCUE-X "
print(raw_info)

# 去除干扰空格
cleaned_info=raw_info.strip()
print(cleaned_info)

# 封装各部分信息
agent_part,coords_part,items_part,mission_part=cleaned_info.split(';')
print(agent_part)
print(coords_part)
print(items_part)
print(mission_part)

# 去除重复装备
items_value=items_part.split(':')[1]
print(items_value)
items_message=items_value.split(',')
print(items_message)
Items=set(items_message)
print(Items)

# 截取核心任务代号
Agent=agent_part.split(':')[1]
print(Agent)

# 锁定坐标
coords_value=coords_part.split(':')[1]
print(coords_value)
cleaned_coords_value=coords_value.strip('()')
print(cleaned_coords_value)
x=int(cleaned_coords_value.split(',')[0])
y=int(cleaned_coords_value.split(',')[1])
Coords=(x,y)
print(Coords)

# 信息归档
Dict={'Agent':Agent,'Coords':Coords,'Items':Items,'Mission':mission_part.split(':')[1]}
print(Dict)