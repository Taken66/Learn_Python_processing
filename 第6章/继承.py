# 题目：基于 Student 定义一个 GradStudent 子类，
# 增加 research\_topic 属性， 重写 \_\_str\_\_ 使其输出包含研究方向。

# 验收标准：

# [ ] 用了继承语法
# [ ] 子类 \_\_init\_\_ 里正确调用了父类 \_\_init\_\_
# [ ] 子类实例同时有父类和自己的属性
# [ ] 重写的 \_\_str\_\_ 生效
# [ ] 能说出 super() 的作用

from 定义类 import  Student

class GradStudent(Student):
    __research_topic = ""
    def __init__(self, name, score, research_topic):
        super().__init__(name, score)
        self.research_topic = research_topic
    def __str__(self):
        return f"{self.name}:{self.score}分，课程：{self.research_topic}"

if __name__ == "__main__":
    people1 = GradStudent("Alice", 85, "Machine Learning")
    print(f"{str(people1)}")
