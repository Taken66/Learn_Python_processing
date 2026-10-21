# 2.2 字符串方法
# 题目：给定 s = " Hello, World! Hello, Python! "，
# 完成： ① 去掉两端空格 ② 全部转小写 ③ 把 "Hello" 替换成 "Hi"
#  ④ 按 "!" 分割成列表 ⑤ 统计 "Hello" 出现次数

# 验收标准：

# [ ] 五个操作各用一个字符串方法完成
# [ ] 结果符合预期
# [ ] 能说出哪些方法是"返回新字符串"而不是"修改原字符串"
s = " Hello, World! Hello, Python! "
print(s)
print(f"去掉两端空格:{s.strip()}")
print(f"全部转小写:{s.lower()}")
print(f'''把"Hello"替换成"Hi":{s.replace("Hello","HI")}''')
print(f"按'!'分割成列表:{s.split('!')}")
print(f"统计'Hello'出现次数:{s.count('Hello')}")
print(s)