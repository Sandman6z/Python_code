# -*- coding: utf-8 -*-

import re

#过滤掉除了中文以外的字符
str = "hello,world!!%[545]你好234世界。。。"
str = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str)
print(str)
  
#提取字符串里的中文，返回数组
pattern="[\u4e00-\u9fa5]+"
regex = re.compile(pattern)
results = regex.findall("adf中文adf发京东方23带手")
print(results)
