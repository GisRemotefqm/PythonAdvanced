# group返回re模块匹配的字符串
# start()返回匹配开始的位置
# end()返回匹配结果的位置
# span()返回一个元集包含匹配(开始，结束)的位置
# 通过match()验证正则

# match("正则表达式", "要验证/检测的字符串")
# 匹配成功返回match object对象
# 匹配失败返回None


import re


result = re.match("\w{4,20}@163\.com$", "hello@163.com")

if result != None:

    print(result)
    print("group:", result.group())
    print("start:", result.start())
    print("end:", result.end())
    print("span:", result.span())
else:
    print(".....")

