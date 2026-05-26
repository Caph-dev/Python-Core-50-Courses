def isPrime(num:int) -> bool:
    if num < 2: return False
    end = int(num **  0.5)
    for x in range(2, end + 1):
        if num % x == 0:
            return False
    return True

def main():
    # 这里要用循环!
    while True:
        try: 
            num = int(input("请输入整数: "))
            break
        except ValueError:
            print("输入类型错误, 请输入整数, 请重新输入.")
    # num = int(input("请输入整数: "))

    if isPrime(num):
        print(f"{num} 是质数")
    else:
        print(f"{num} 不是质数")

# 只有当这个 Python 文件被“直接运行”时，下面的代码才会执行
if __name__ == "__main__": 
    main()