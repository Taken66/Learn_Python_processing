
# 题目：给 Student 加一个类属性 school = "某某大学"， 
# 创建两个实例，分别修改其中一个的 school，观察另一个是否受影响。

# 验收标准：

# [ ] 能演示出"改实例属性不影响类属性"和"改类属性影响所有实例"
# [ ] 能说出类属性和实例属性的区别与适用场景
# ---
class Student:
    school = "西巴大学"
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name}:{self.score}分"

s1 = Student("111",111)
s2 = Student("222",222)
print(f'''
 ===========开始==========
{s1.school}
{s2.school}


''')

s1.school="某某大学"
print(f'''
=====修改s1的实例属性====
{s1.school}
{s2.school}
{s1.__dict__}
''')


del s1.school
Student.school="cq大学"
print(f'''
=====修改所有的实例属性====
{s1.school}
{s2.school}

''')