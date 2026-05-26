"""
b = (1,2,5)
print(b)
"""
b = (1,2,5)
print(b) # (1, 2, 5)

# 写法注意: 只有一个元素时, 需要加一个逗号, 否则会被认为是整数
a = (1)
print(type(a))  # <class 'int'>
b = (1,)
print(type(b))  # <class 'tuple'>

# 常用方法: index, count
t = (1, 2, 3, 1, 2, 3)
print(t.index(2))  # 1, 返回第一个2的索引
print(t.count(3))  # 2, 返回3的个数

# 作为字典的 key
d = {}
d[(1,2)] = "key"
print(d) # {(1, 2): 'key'}

# 适用场景: 数据固定不变, 坐标/配置/返回多个值
point = (10,20)
rgb = (255, 255, 255)

def get_user():
    return "Alice", 20
print(get_user()) # ('Alice', 20)
print(type(get_user())) # <class 'tuple'>