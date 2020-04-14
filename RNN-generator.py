import math
import re
import numpy as np
import tensorflow as tf
from collections import Counter

#数据预处理
DATA_PATH = 'shi.txt'
MAX_LEN = 64
# 禁用的字符，拥有以下符号的诗将被忽略
DISALLOWED_WORDS = ['（', '）', '(', ')', '__', '《', '》', '【', '】', '[', ']']

# 一首诗（一行）对应一个列表的元素
poetry = []

# 按行读取数据 poetry.txt
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()
# 遍历处理每一条数据
for line in lines:
    # 利用正则表达式拆分标题和内容
    fields = re.split(r"[:：]", line)
    # 跳过异常数据
    if len(fields) != 2:
        continue
    # 得到诗词内容（后面不需要标题）
    content = fields[1]
    # 跳过内容过长的诗词
    if len(content) > MAX_LEN - 2:
        continue
    # 跳过存在禁用符的诗词
    if any(word in content for word in DISALLOWED_WORDS):
        continue

    poetry.append(content.replace('\n', '')) # 最后要记得删除换行符

######################

for i in range(0, 5):
    print(poetry[i])