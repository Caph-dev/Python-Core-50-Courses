"""
a = [[1,2], [3,4]]
1. 赋值: b = a ==> b 和 a 指向同一个列表对象。
2. 浅拷贝: b = a.copy()
    a is not b
    a[0] is b[0]
3. 深拷贝: b = copy.deepcopy(a)
"""
import copy
a = [[1,2], [3,4]]
b1 = a
b2 = a.copy()
b3 = copy.deepcopy(a)

print(f"{a is b1=}")
print(f"{a is b2=}")
print(f"{a is b3=}")

print(f"{a[0] is b1[0]=}")
print(f"{a[0] is b2[0]=}")
print(f"{a[0] is b3[0]=}")

b2[0][0] = 100
print(f"{a=}")
print(f"{b1=}")
print(f"{b2=}")
print(f"{b3=}")