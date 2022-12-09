# 从文本中找出连续出现的重复单词


import re

test_str = "the little cat cat in the hat hat."
re.sub(r'(\w+) \1', r'\1', test_str)
