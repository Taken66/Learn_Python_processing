# 题目：写一个函数 describe(name, age, city="北京")，返回格式化字符串；
# 再写一个函数 stats(numbers)，返回最大值、最小值、平均值（返回三个值）。

# 验收标准：

# [ ] describe 有默认参数，不传 city 时用默认值
# [ ] stats 一次返回三个值，调用处能解包接收
# [ ] 能说出位置参数和关键字参数的区别
# [ ] 给 stats 加注释说明参数类型和返回类型（用类型注解）

def describe(name, age, city="北京"):
    return (f"姓名：{name}，年龄:{age},来自:{city}")

def stats(numbers):
    return max(numbers),min(numbers),sum(numbers)/len(numbers)

print(describe("张三",13,"南宁"))
numbers = (1,2,3,4,5,6)

print(stats(numbers))