
# 题目：给定字典列表（用 3.6 的数据），
# 用 sorted() + lambda 实现： ① 按年龄升序 ② 按分数降序 ③ 按姓名长度排序
# 姓名   年龄  分数
# 张三   25    87
# 李四   30    92
# 王五   28    78
# 验收标准：

# [ ] 三次排序都用 key=lambda 实现
# [ ] 结果正确
# [ ] 能说出 key 参数接收的是什么

a = [{"name" : "张三","age" : 25, "score" : 87},
     {"name" : "李四","age" : 30,"score" : 92},
     {"name" : "王五","age" : 28,"score" : 78}]

print(f'''
按照年龄升序排列：{sorted(a,key = lambda x : x["age"],reverse = False)}

按分数降序: {sorted(a,key = lambda x :x["score"],reverse = True)}
按姓名长度排序 :{sorted(a,key = lambda x :len(x["name"]))}

''')