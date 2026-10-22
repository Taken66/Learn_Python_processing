class Experiment:
    def __init__(self,name,seed):
        self.name = name
        self.seed = seed
        self.results = []

    def add_result(self,value) :
       
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
