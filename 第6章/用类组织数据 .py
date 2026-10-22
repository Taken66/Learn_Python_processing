# 题目：定义一个 Experiment 类，表示一次实验：

# 属性：name、seed、results（列表）
# 方法：add\_result(value) 添加结果
# 方法：mean() 返回平均值
# 方法：summary() 返回一行摘要字符串
# 验收标准：

# [ ] 创建实例、添加若干结果、求平均、打印摘要，全部正常
# [ ] mean() 在 results 为空时要不崩溃（返回值或抛异常，你自己决定并说明理由）
# [ ] 能说出为什么用类比用字典更适合表示"一次实验"

class Experiment:
    def __init__(self,name,seed):
        self.name = name
        self.seed = seed
        self.results = []

    def add_result(self,value) :
        #value = float(input("请输入实验结果："))
        self.results.append(value)
    
    def mean(self):
        try :
            return sum(self.results) / len(self.results)
        except ZeroDivisionError:
            return "results是空的"

    def summary(self) :
        return f"实验名称：{self.name} ,种子：{self.seed},平均率：{self.mean()} "

if __name__ == "__main__":
    E1 = Experiment("SVM",42)
    print(E1.summary())
    E1.add_result(6.5)
    E1.add_result(5.6)
    print(E1.summary())


