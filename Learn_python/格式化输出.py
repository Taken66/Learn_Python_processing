

# 题目：给定 name = "张三"、age = 25、score = 87.456，用三种方式输出同一句话：
#  张三 今年 25 岁，得分 87.46# 验收标准：

# [ ] 三种方式分别是：% 格式化、str.format()、f-string
# [ ] 得分保留两位小数，且是四舍五入
# [ ] 三行输出完全一致

name = "张三"
age = 25
score = 87.456

print("%s 今年 %d 岁，得分 %.2f" %(name,age,score))

print("{} 今年 {} 岁，得分 {:.2f}".format(name,age,score))

print(f"{name} 今年 {age} 岁，得分 {score:.2f}")


