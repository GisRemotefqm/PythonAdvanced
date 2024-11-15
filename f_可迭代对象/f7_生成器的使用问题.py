# 创建生成器
def fibnacci(n):
    # 第一列和第二列

    a = 1
    b = 1

    current = 0

    while current < n:

        data = a
        a, b = b, a + b
        current += 1
        # yield可以充当return的作用
        # yield能够保存程序的状态（相当于在while循环中终止，下一次next()时进入下一次循环）
        yield data
        xxx = yield data


        if xxx == 5:
            # 可以让生成器不再生成
            return "刘必友是傻逼"

if __name__ == "__main__":
    fib = fibnacci(9)

    value = next(fib)
    print(value)

    # 可以用于传参，判断
    value = fib.send(5)


    try:
        value = next(fib)
        print(value)
    except Exception as e:
        print(e)