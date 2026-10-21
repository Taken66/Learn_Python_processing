# 题目：把下面的表格用"列表套字典"表示并打印：
# 姓名   年龄  分数
# 张三   25    87
# 李四   30    92
# 王五   28    78
# 然后：① 找出分数最高的人 ② 按分数降序排序 ③ 计算平均分

# 验收标准：

# [ ] 数据结构是 \[{"name":..., "age":..., "score":...}, ...]
# [ ] ① 用 max() 配合 key 参数实现
# [ ] ② 用 sorted() 配合 key 和 reverse 参数
# [ ] ③ 平均分保留一位小数
# ---

a = [{"name" : "张三","age" : 25, "score" : 87},
     {"name" : "李四","age" : 30,"score" : 92},
     {"name" : "王五","age" : 28,"score" : 78}]

c = max(a,key=lambda x: x["score"])
print("分数最高的人是：",c.get("name"))
print("按分数降序排序:",sorted(a,key = lambda x : x["score"],reverse = True))
sum_a = sum([x["score"] for x in a ])
ave = sum_a / len(a)
print(f"平均分{ave:.1f}")

