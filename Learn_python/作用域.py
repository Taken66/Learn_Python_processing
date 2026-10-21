
# 题目：写一段代码演示：函数内修改全局变量、
# 函数内使用局部变量、以及在函数内用 global 声明。

# 验收标准：

# [ ] 能正确打印出"没有 global 时的结果"和"有 global 时的结果"的差异
# [ ] 能说出为什么不推荐用 global
# [ ] 能说出 LEGB 规则的顺序
# ---
x  = 10 #全局
def fun ():
   y = 11 #局部
   global x
   x += 1
   print(x)
   print(y)
fun()
print(x)
print(y) #(无法调用局部变量)

