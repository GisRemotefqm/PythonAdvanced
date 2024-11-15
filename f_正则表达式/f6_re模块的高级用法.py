# search，sub，split findall方法的使用
# 在爬虫中经常使用

import re

# search()方法，搜索匹配, 会在字符串中搜索相应字符串
result = re.search("hello", "asdhello@163.com")
print(result)


# findall()搜索全部，返回列表
result = re.findall("\d+", "阅读次数：9999，评论次数99998")
print(result)


# sub字符串替换，查找字符串后替换为指定内容
result = re.sub("he", "she", "asdhello@163.com")
print(result)

str1 = """
    <h1>asdfasdfasfdafdadsfasgasfasfafdadfasdf</h1>
    sadffdafasdfasfasdfa
    asdfsafsfiojklnuh'jlnukkfaf
    knzxfaifojzkjfaof

"""
print(str1)


# split拆分字符串
result = re.split(":| ", "info:hello@163.com zhangsan")
print(result)