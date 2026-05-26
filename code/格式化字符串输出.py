"""
最常用的格式化字符串输出:
1. f-string: f"{变量}" 和 f"{变量:格式}"
2. 调试写法: print(f"{变量=}")
3. 格式化字符串: print("%d * %d = %d" % (a, b, a * b))
"""

name = "Alice"
score = 98.76
age = 18

print(f"{name} 的成绩是 {score:.2f}")
print(f"{name=}, {age=}, {score=}")
print("%s 的年龄是 %d" %(name, age))
