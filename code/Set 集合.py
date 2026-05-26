"""
无序: 输出顺序不一定
不重复
元素必须是可哈希的: 不可变类型(int, str, tuple), 不能存可变类型(list, dict, set)

"""

# 创建集合 {}
st = {1, 2, 3, 4, 5}
# 创建集合的构造器语法
st = set([1, 2, 3, 4, 5])
# 创建集合的生成式语法
st = {i*i for i in range(1, 10) if i%2 == 0}
print(st)


## 用途 1: 去重
lst = [1,1,2,3,4,5]
st = set(lst)
print(st)
# 转为列表:
lst = list(st)
print(lst)

# 增加元素: add, update
st.add(6) # 增加单个元素
st.update([7,8,9]) # 增加多个元素
print(st)

# 删除元素: remove, discard, pop
## remove: 删除指定元素, 如果元素不存在, 会引发 KeyError 异常
st.remove(9)
#st.remove(10) # KeyError: 10
## discard: 删除指定元素, 如果元素不存在, **也不会引发异常**
st.discard(10)
print(st)
## pop: 删除并返回一个随机元素(因为无序, 所以随机)
e = st.pop()
print(e)
print(st)

# 清空集合: clear
st.clear()
print(st)

# 判断元素是否在集合中: in, not in
print(1 in st)
print(10 in st)
print(10 not in st)

# 集合的运算: &, |, -, ^
# 并集: a | b == a.union(b)
# 交集: a & b == a.intersection(b)
# 差集: a - b == a.difference(b)
# 对称差: a ^ b == a.symmetric_difference(b) 只属于其中一个集合的元素

st1 = {1,2,3}
st2 = {2,3,4}
print(st1 & st2) # {2,3}
print(st1 | st2) # {1,2,3,4}
print(st1 - st2) # {1}
print(st1 ^ st2) # {1,4}

# 集合的比较运算: ==, !=, <, <=, >, >=
# ==: 两个集合完全相同
# !=: 两个集合不完全相同
# <: 第一个集合是第二个集合的**真**子集
# <=: 第一个集合是第二个集合的**子集**
# >: 第一个集合是第二个集合的**真**超集
# >=: 第一个集合是第二个集合的**超集**
print(st1 == st2) # False
print(st1 != st2) # True
print(st1 < st2) # False
print(st1 <= st2) # False
print(st1 > st2) # False
print(st1 >= st2) # True

# frozenset: 不可变集合
st = frozenset([1,2,3,4,5])
print(st)
print(type(st)) # <class 'frozenset'>

# 不支持增删改查操作
# 不可变集合的运算: &, |, -, ^
print(st & st)
print(st | st)
print(st - {1})
print(st ^ (st | {9}))