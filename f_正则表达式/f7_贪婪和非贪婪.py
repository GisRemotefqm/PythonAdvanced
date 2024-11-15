# python中默认是贪婪得，即当条件满足是尝试尽可能多的截取内容

import re

result = re.match("aaa\d+", "aaa123456")
print(result)

# 改为非贪婪使用符号？,在+*?()后面加上问号即可改为非贪婪

result = re.match("aaa\d+?", "aaa123456")
print(result)

