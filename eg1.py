#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : eg1.py
# @Software: PyCharm
"""
the first example for nltk book
"""
from nltk.book import *


# 查找特定词语上下文
# text1.concordance("monstrous")

# 相关词查找
# text1.similar("monstrous")

# 查找多个词语的共同上下文
# text2.common_contexts(["monstrous", "very"])

# 画出词语的离散图
# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# 产生随机文本
# text3.generate()
# Traceback (most recent call last):
#   File "E:/nlp/eg1.py", line 25, in <module>
#     text3.generate()
# TypeError: generate() missing 1 required positional argument: 'words'

# 单词数量 标识符总数
# print(len(text3))

# 词汇的种类及数量 用集合set显示
# print(sorted(set(text3)))
# print(len(set(text3)))

# 测量平均每类词语被使用的次数
# from __future__ import division #本命令必须放在文件的开始之初
# print(len(text3)/len(set(text3)))

# 统计特定单词在文本中出现的次数，并计算其占比
# print(text3.count("smote"))
# print(100*text4.count('a')/len(text4))

# 词的频率分布
fdist1 = FreqDist(text1)
# 输出总的词数
print(fdist1)
# In Python 3 dict.keys() returns an iteratable but not indexable object.
vac1 = list(fdist1.keys())
# 输出词数最多的前五十个词
print(vac1[:50])
# 输出whale的次数
print(fdist1["whale"])
# 输出前五十个词的累积频率图

fdist1.plot(50)