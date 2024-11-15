# 创建生成器
def fibnacci(n):
    # 第一列和第二列

    a = 1
    b = 1

    current = 0

    while current < n:

        data = a
        a, b = b, a + b

        # yield可以充当return的作用
        # yield能够保存程序的状态（相当于在while循环中终止，下一次next()时进入下一次循环）
        yield data

if __name__ == "__main__":

    fib = fibnacci(9)

    value = next(fib)
    print(value)

    value = next(fib)
    print(value)

    value = next(fib)
    print(value)

    value = next(fib)
    print(value)

    value = next(fib)
    print(value)