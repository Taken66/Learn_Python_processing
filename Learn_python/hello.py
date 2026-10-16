# 写一个 hello.py，运行时打印你的名字和当前日期。

# 验收标准：

# [ ] 文件扩展名是 .py
# [ ] 用 python hello.py 能运行
# [ ] 输出包含名字和日期两部分

import time
myname = input("What is your name? \n")
print(f"hello,{myname},now {time.strftime('%Y-%m-%d-%H-%M',time.localtime())}")




