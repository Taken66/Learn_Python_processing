
# 题目：写一个脚本读取一个不存在的文件，要求程序不崩溃，而是打印友好提示。

# 验收标准：

# [ ] 捕获了正确的异常类型（不是笼统的 Exception）
# [ ] 打印的提示包含文件名
# [ ] 能说出 try/except/else/finally 四个块各自什么时候执行


file_name = input("输入文件名")
try :
    with open(f"{file_name}","r",encoding = "utf-8") as f:
       reader = f.readlines()
except FileNotFoundError :
    print(f"文件{file_name}不存在")
else :
     print(reader)
finally :
    print("结束")