from pickletools import floatnl

from experiment_package import Experiment, safe_divide


x1 = Experiment("test",12)
 
for i in range(1,4):    
    x1.add_result(float(input("请输入实验结果：")))
print(x1.summary())

print(safe_divide(10, 0) )