# 题目：d = {"name": "张三", "age": 25}，完成：
# ① 安全地取 city 键（不存在时返回 "未知"）
# ② 添加 city: 北京 
# ③ 遍历打印所有键值对 
# ④ 删除 age 
# ⑤ 把两个字典 {"a":1} 和 {"b":2} 合并

# 验收标准：

# [ ] ① 用了 get() 而不是 \[]
# [ ] ③ 遍历时同时拿到 key 和 value
# [ ] ⑤ 用了两种方法（update 和 | 或解包）都试一遍
# [ ] 能说出为什么 d\["city"] 会报错而 d.get("city") 不会
d = {"name": "张三", "age": 25}

print(d.get('city',None))
d['city'] = "北京"
print(d)

for k ,v in d.items():
    print(k,v,end=' ')

del d["age"]
print("\n删除age后的：",d)
a={"a":1} 
b={"b":2}
a.update(b)
print(f"合并后：{a}")