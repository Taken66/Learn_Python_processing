# 题目：s = "Multi-Objective Evolutionary Algorithm"，
# 用切片取出： ① 前 5 个字符 ② 后 9 个字符 ③ 第 6 到第 15 个字符 ④ 整个字符串倒序

# 验收标准：

# [ ] 四个都用切片实现，不用循环
# [ ] 倒序只用了切片（提示：步长）
# [ ] 能说出切片 \[a:b] 是"左闭右开"
s = "Multi-Objective Evolutionary Algorithm"
print(s[0:5])
print(s[-9:])
print(s[5:15])
print(s[::-1])