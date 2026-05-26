"""
range 的用法:
range(stop) = range(0,stop)
range(start, stop) => start 到 stop-1
range(5, -1, -1) => 5,4,3,2,1,0
"""

print("range(5, -1, -1) => 5,4,3,2,1,0")
for x in range(5,-1,-1):
    print(x)
print("---")

r = range(0,5)
print(f"r=range(0,5) 的打印结果是 {r}")
print(f"list(range(0,5))的打印结果是{list(r)}")
print("---")