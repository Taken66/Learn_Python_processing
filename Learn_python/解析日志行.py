# 题目：给定一行文本： 2026-10-08 14:30:22 ERROR \[main] 数据加载失败: file not found 
# 用字符串方法提取出：日期、时间、日志级别、错误信息

# 验收标准：

# [ ] 四个部分都正确提取
# [ ] 只用了字符串方法（split/切片/index），没用正则
# [ ] 能说出如果日志格式变了，你的代码哪里会挂

import re

s = "2026-10-08 14:30:22 ERROR [main] [what]数据加载失败: file not found "
# y=r'\d{4}-\d{2}-\d{2}'
log = s.split(' ',3)
print(log)
info = log[-1].split("]")
print(info)
print(log)
print(f'''日期:{log[0]}
时间:{log[1]}
日志级别:{log[2]}
错误信息:{info[-1]}''')
# print(f'日期:{re.search(y,s).group()} ')