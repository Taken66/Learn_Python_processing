
# 题目： ① 打印当前日期时间 
# ② 格式化成 2026-10-08 14:30:22 形式
# ③ 计算从今天起 100 天后的日期 
# ④ 生成一个"带时间戳的文件名"

# 验收标准：

# [ ] ①②③④ 全部正确
# [ ] ③ 用了 timedelta
# [ ] ④ 的时间戳格式是 20261008\_143022 这种（不含冒号，因为文件名不能用冒号）
# [ ] 能说出 strftime 和 strptime 的区别

from datetime import datetime,time,date, timedelta
import time

now = datetime.now()
print(now)

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

date_100 = now + timedelta(days = 100)
print(f"100天后：{date_100}")

import os
now_1 = time.strftime("%Y%m%d_%H%M%S",time.localtime())
print(os.getcwdb())

os.chdir("第8章")
os.mkdir(f"{now_1}")



