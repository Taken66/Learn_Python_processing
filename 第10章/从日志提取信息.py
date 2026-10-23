# 给一段多行日志文本（自己编造，含时间、级别、消息），
#  用正则提取出所有 ERROR 级别的行，并统计各日志级别各出现了几次。

# 验收标准：

# [ ] 提取结果正确
# [ ] 统计结果用字典或 Counter 表示
# [ ] 能说出如果你的正则写得太宽松，会有什么问题
import os,re 
from collections import Counter 
print(os.getcwdb())

with open(r"E:\VS_tools\Project\Learn_python\第10章\日志","r",encoding="utf-8") as f:
   reader = f.readlines()


pu = "".join(reader)
print(pu)
# print(pa.findall(pu))
pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| (\w+) +\| (.*)")

print(re.findall(r"(\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})\s*\|\s*(ERROR)\s*\|\s*(.*)",pu))
p = r"(ERROR|INFO|DEBUG|WARNING|CRITICAL)" 
p1 = re.findall(p,pu)
print(Counter(p1))
