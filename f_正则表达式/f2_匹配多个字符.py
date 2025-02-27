# *是匹配前一个字符出现0次或者无限次，即可有可无
# +匹配前一个字符出现1次或无数次
# ? 匹配前一个字符出现1次或者0次

# {m]}匹配前一个字符出现m次

# 示例：
# 1. 匹配第一个字符为大写后面任意多个小写字符
# [A-Z][a-z]*

# 2. 匹配变量名是否有效
# [a-zA-Z_]+\w

# 3.匹配出0-99之间的数字
# [0-9]?[0-9]

# 4. 判断不以4和7结尾的手机号手机号
# [0-9]{10}[12356890]
# {5,20}是在这个范围的次数

# \为转义字符，\.表示. 