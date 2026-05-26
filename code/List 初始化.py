"""
外层用 * 复制可变对象时，复制的是引用，不是对象本身。
二维列表初始化优先用列表推导式。

错误: scores = [[0] * 3] * 5 ==> 5 个引用指向同一个列表对象。
含义: row = [0, 0, 0]
      scores = [row, row, row, row, row]

正确: scores = [[0] * 3 for _ in range(5)]
含义: scores = []
      for _ in range(5):
          scores.append([0, 0, 0])
"""