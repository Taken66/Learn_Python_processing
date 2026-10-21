
# 题目：写一个脚本： 
# ① 把 1–10 每个数字的平方写入 squares.txt（每行一个）
# ② 读回该文件并打印所有内容 
# ③ 统计文件有多少行

# 验收标准：

# [ ] 写入和读取都用 with open()（不许用 open() 后忘记 close）
# [ ] 写入时用了换行符
# [ ] ③ 的行数正确
# [ ] 能说出 with 相比手动 close 的好处
import os
with open("E:/squares.txt","w+") as f:
    for i  in range(1,11):
        f.write(f"{i**2}\n")
    f.seek(0)
    lines = f.readlines()
    print(lines)
    print([i.strip("\n") for i in lines])
    print(f"文件行数:{len(lines)}")
    
# 题目：在 5.1 生成的文件末尾追加 11–15 的平方，然后重新读取确认有 15 行。
# 验收标准：
# [ ] 用了正确的文件模式（不是 w，而是追加模式）
# [ ] 重新读取后行数是 15
# [ ] 能说出 r / w / a / r+ 四种模式的区别（以及 w 的危险性）

with open("E:/squares.txt","a+") as f:
    for i in range(11,16):
        f.write(f"{i**2}\n")

    f.seek(0)
    lines_1 = f.readlines()
    print([i.strip("\n") for i in lines_1])
    print(f"文件行数:{len(lines_1)}")