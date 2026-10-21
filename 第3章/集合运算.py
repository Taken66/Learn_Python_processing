# 题目：a = {1, 2, 3, 4}，b = {3, 4, 5, 6}，
# 求： 交集、并集、差集（a 有 b 没有）、对称差集

# 验收标准：
# [ ] 四个结果正确
# [ ] 用运算符和方法各写一遍（如 \& 和 intersection）
# [ ] 给定 \[1,1,2,3,3,3]，用集合去重并保持类型是列表
# ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f'''
交集:{a | b}
并集:{a & b}
差集:{a - b}
对称差集:{a ^ b}
''')
print(f'''
交集:{a.union(b)}
并集:{a.intersection(b)}
差集:{a.difference(b)}
对称差集:{a.symmetric_difference(b)}
''')

c = [1,1,2,3,3,3]
d=set(c)
print(list(d))