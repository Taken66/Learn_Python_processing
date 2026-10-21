# 用 csv 模块： 
# ① 把下面的数据写成 people.csv（带表头）
# ② 读回并打印
# ③ 读回时算出年龄总和
# 验收标准：
# [ ] 写入用了 csv.writer 或 DictWriter
# [ ] 读回用了 csv.reader 或 DictReader
# [ ] 打开文件时指定了 newline=""（并知道为什么）
# [ ] ③ 注意读到的是字符串，做了类型转换
# 姓名   年龄  分数
# 张三   25    87
# 李四   30    92
# 王五   28    78

import csv
filed = ["name","age", "score" ]
a = [{"name" : "张三","age" : 25, "score" : 87},
     {"name" : "李四","age" : 30,"score" : 92},
     {"name" : "王五","age" : 28,"score" : 78}]

# with  open("people.csv",mode="w+",encoding="utf-8",newline="") as f:
#     writer  = csv.DictWriter(f,fieldnames = filed)
#     writer.writeheader()
#     writer.writerows(a)
    
# with open("people.csv","r",encoding="utf-8",newline= "") as f :
#     reader = csv.DictReader(f)
#     header = reader.fieldnames
#     print(header)
#     for row in reader:
#         print(row["name"],row["age"],row["score"])

with open("people.csv","r",encoding="utf-8",newline= "") as f :
    reader = csv.reader(f)
    header = next(reader) # next()读取第一行，就是表头
    print(header)
    # 剩下循环就是数据行
    for row in reader:
        print(row)
