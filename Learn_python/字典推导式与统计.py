# 题目：给定字符串 s = "abracadabra"，用字典统计每个字母出现的次数。
# 验收标准：
# [ ] 结果正确（a:5, b:2, r:2, c:1, d:1）
# [ ] 至少用两种写法：普通 for 循环 + 字典推导式或 Counter
# [ ] 能说出哪种写法更 Pythonic

s = "abracadabra"
b = {}
for i in s:
    if i in b:
        b[i] += 1
    else :
        b[i] = 1
print(b)

a = {x:0 for x in s  }
for i in s:
    a[i] += 1
print(a)


from collections import Counter
c = Counter(s)
print(c)
