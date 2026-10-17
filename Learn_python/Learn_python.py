# # import numpy as np
# # a = np.random.randn(4, 3)
# # b = np.random.randn(3, 5)
# # c = a @ b 
# # print(a)
# # print(b)
# # print(f"a @ b = \n{c}")
# # assert c.shape == (4, 5)

# # pool_demo.py
# from multiprocessing import Pool
# import os, time

# def long_task(name):
#     print(f'任务{name} pid={os.getpid()}')
#     time.sleep(1)
#     return name

# if __name__ == '__main__':
#     p = Pool(4)
#     res = [p.apply_async(long_task, args=(i,)) for i in range(5)]
#     p.close()
#     p.join()
#     for r in res:
#         print(r.get())


#第一题给字符串 `"Hello 世界 123! @#$"`，分别统计字母、数字、空格、其他四类字符的个数
#，并验证四类之和等于字符串长度。
#考察点：`isalpha` / `isdigit` / `isspace`、生成器表达式配合 `sum`
#提示：Python 的 `str.isalpha()` 对汉字也返回 `True`，注意这一点。


# X = 'Hello 世界 123! @#$'
# digit = 0
# space = 0
# alpha = 0
# chinese = 0
# other = 0
# for i in X :
#     if i.isdigit() :
#         digit += 1
#     elif i.isspace() :
#         space += 1
#     elif '\u4e00' <= i <= '\u9fff' :
#         chinese += 1
#     elif i.isalpha()  and  i.isascii():
#         alpha += 1
#     else :
#         other += 1
# print(f'字母个数：{alpha}，数字个数：{digit}，中文个数：{chinese},空格个数：{space}，其他字符个数：{other}')

# #第二题
# # 把 `\[3,1,2,3,5,1,2,4]` 去重，保持元素第一次出现的顺序，输出 `\[3,1,2,5,4]`。写出两种实现并比较优劣。
# # 考察点：`dict.fromkeys`、`set`、`sorted(key=...)`
# # 提示：`set` 会丢顺序；`sorted(set(x), key=x.index)` 虽然能做，但 `list.index` 是 O(n)，长列表上很慢。

# arr = [3,1,2,3,5,1,2,4]
# print(f"第一种方法list(dict.fromkeys())：{list(dict.fromkeys(arr))}")
# print(f"第二种方法sorted：{sorted(set(arr),key =  arr.index)}")

# 第三题
# `d1 = {"a":1,"b":2,"c":3}`、`d2 = {"b":10,"c":20,"d":30}`，
# 合并成 `{"a":1,"b":12,"c":23,"d":30}`。用三种写法实现。
# 考察点：`dict.get`、`items()`、`collections.Counter`、
# 字典推导式与 `keys() | keys()`
# 提示：`Counter` 支持直接相加，最简洁；
# 推导式写法要考虑两个字典键集合的并集。

# from collections import Counter

# d1 = {"a":1,"b":2,"c":3}
# d2 = {"b":10,"c":20,"d":30}

# d3 = dict(Counter(d1) + Counter(d2))
# print(f"使用Counter：{d3}")

# d3 = {i : d1.get(i,0) + d2.get(i,0)  for i in sorted(d1.keys() | d2.keys())}
# print(f"字典推导式：{d3}")
# d3_keys =  d1.keys() | d2.keys()
# d3 = {}
# for k in sorted(d3_keys):
#     d3[k] = d1.get(k,0) + d2.get(k,0)

# print(f"get相加后：{d3}")

# import time

# for i in range(101): # 添加进度条图形和百分比
#     bar = '[' +  '='  * (i // 2) + ' ' * (50 - i // 2) + ']'
#     print(f"\r{bar} {i:3}%", end='', flush=True)
#     time.sleep(0.05)
# print()

# d = {"name": "张三"}
# print(d.__getitem__)   # [] 用的是这个
# print(d.get)           # get 是独立的方法

# try:
#     d["city"]
# except Exception as e:
#     print(type(e).__name__, "->", e)


#     s = "a  b"
# print(s.split())        # 不带参数
# print(s.split(' '))     # 带单个空格
# print(len(s.split()), len(s.split(' ')))


# t = "  a  b  "
# print(t.split())
# print(t.split(' '))


# for v in ["False", "0", "None", " ", "", 0, 0.0, -1]:
#     print(f"{v!r:10} -> {bool(v)}")
# print("a\tb\nc".split())

# print("a\tb\nc".split(' '))

# names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
# # new_names = [name.upper()for name in names if len(name)>3]
# # print(new_names)
# # ['ALICE', 'JERRY', 'WENDY', 'SMITH']
# #迭代式子
# a = iter(names)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# def test(*args):
#     print(args)

# test(1,2,3)
# test([1,2,3])
# test(*[1,2,3])

# def test(func):
#     def wrapper(*args):
#         print("开始")
#         x = func(*args)
#         print("结束")
#         return x
#     return wrapper

# @test
# def func(*args):
#     print("???",*args)
# a= [1,2,3]
# func(a)

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"函数{func.__name__}耗时：{end-start:.4f}秒")
#         return result
#     return wrapper

# @timer
# def test(n):
#     s = 0
#     for i in range(n):
#         s += i
#     return s

# print(test(1000000))
# print(__file__)

# import math
# print(dir(math))
import os

print(os.getcwd())


with open("E:/text.txt","r",encoding = "UTF-8") as f:
    #f.write("我日了")
    line = f.readlines()
    print(f.tell)
print(line)

