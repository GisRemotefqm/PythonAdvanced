import re

# r的作用是让正则表达式中的\没有特殊含义
result = re.match(r"<([a-zA-Z0-9]+)>.*</\1>", "<html>baidu,com</html>")
print(result)