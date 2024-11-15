# |的作用是: 匹配左右任意一个表达式
# ()的作用是：将括号中字符作为一个分组
# \的作用是：引用(分组num)匹配到字符串
import re

# 判断0-100之间的数字
result = re.match("^[0-9]?[0-9]$|^100$", "68")
print(result)


# 匹配邮箱如163，qq等
result = re.match("\w{4,20}@(163|126|qq)\.com$", "hello@163.com")
print(result)

# ()有分组的功能，第一个默认为1以此类推
print(result.group(1))

# /的用法
result = re.match("<([a-zA-Z0-9]+)>.*</\\1>", "<html>baidu,com</html>")
print(result)

# /使用别名的方法
# ?P<name>起别名，(?P=name)用别名
result = re.match("<(?P<name1>[a-zA-Z0-9]+)>.*</(?P=name1)>", "<html>baidu,com</html>")
print(result)
