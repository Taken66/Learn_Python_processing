
# 题目：写一个函数 sum\_all(\*args) 能接收任意个数字并返回总和；
#  再写一个 print\_info(\*\*kwargs) 能接收任意关键字参数并逐行打印。

# 验收标准：

# [ ] sum\_all(1,2,3) 和 sum\_all(1,2,3,4,5) 都能正确返回
# [ ] print\_info(name="张三", age=25) 输出两行
# [ ] 能说出 \*args 和 \*\*kwargs 各自接收到的是什么类型

def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")


a = (1,2,3)
print(f"返回总和：{sum_all(*a)}")
print_info(name="张三", age=25)

#print(dict(name="张三", age=25))