
# 题目：写一个函数 safe\_divide(a, b)： 
# ① 正常相除 
# ② 分母为 0 时返回 "除数不能为0" 而不是崩溃 
# ③ 参数不是数字时返回 "参数类型错误"

# 验收标准：

# [ ] safe\_divide(10, 2) → 5.0
# [ ] safe\_divide(10, 0) → "除数不能为0"
# [ ] safe\_divide("a", 2) → "参数类型错误"
# [ ] 用了两个不同的 except 捕获不同异常
# [ ] 能说出 except Exception 为什么太宽泛

def safe_divide(a, b):
    try :
        return a / b
    except ZeroDivisionError :
        return "除数不能为0"
    except TypeError:
        return "参数类型错误"

print(safe_divide(10, 2) )
print(safe_divide(10,0 ) )
print(safe_divide("m", 2) )

