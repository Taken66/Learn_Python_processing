
# 题目：定义一个 Student 类：

# 属性：name、score
# 方法：is\_pass() 返回是否及格（≥60）
# 方法：\_\_str\_\_ 返回 "张三: 87分"
# 验收标准：

# [ ] 有 \_\_init\_\_ 方法，用 self 赋属性
# [ ] is\_pass() 能被调用并返回布尔值
# [ ] print(实例) 输出的是 \_\_str\_\_ 的返回值（不是一串内存地址）
# [ ] 能说出 self 是什么
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name}:{self.score}分"

if __name__ == "__main__":
    T=Student("张三", 87)
    print(str(T))

