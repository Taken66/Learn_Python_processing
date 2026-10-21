# 题目：写一个脚本：
# ① 在 data/ 目录下创建 3 个文本文件
# ② 遍历该目录，读每个文件 
# ③ 打印每个文件的文件名和内容长度
# ④ 遇到读不了的文件要跳过并记录
# 验收标准：
# [ ] 目录不存在时能自己创建（用 os.makedirs 或 pathlib）
# [ ] 用 os.listdir 或 pathlib.Path.glob 遍历
# [ ] 每个文件的信息都打印出来
# [ ] ④ 在循环内做了异常处理，一个文件失败不影响其他文件


import os

if os.path.exists('data'):
    print("目录存在，已切换近data文件里\n")
    os.chdir("data")
else :
    os.mkdir("data")
    print("目录创建成功，已切换近data文件里\n")
    os.chdir("data")
print(os.getcwdb())
print(os.listdir())
T = "\n"
for i in  os.listdir():
   if os.path.isfile(i):
        try :
            with open(i,"r",encoding="utf-8") as f:
                reader = f.readlines()
        except Exception as e:
            print(f"读取失败的文件名字:{i},错误信息:{e}")
        else :
            print(f'''文件名字：{i} \n 内容：{[row.strip(T) for row in reader]}
''')
        finally :
            print("\n读取完毕！！！")
   else :
        print("这是文件夹{}".format(i))

    


