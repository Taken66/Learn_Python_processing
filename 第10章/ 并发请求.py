# 题目：模拟"需要请求 10 次网络接口"的场景（可以用 time.sleep(1) 模拟）
# ， 写两个版本：① 串行 
# ② 并发。比较两者的耗时。

# 验收标准：

# [ ] 串行版本耗时约 10 秒
# [ ] 并发版本耗时约 1 秒（这是关键）
# [ ] 并发用了 ThreadPoolExecutor
# [ ] 能说出为什么调用大模型 API 必须用并发
# import time 
# import threading
# class Test(threading.Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print("开始{}\n".format( self.name))
#         time.sleep(1)
#         print("结束{}\n".format( self.name))



# def test(name):
#     print("开始{}\n".format(name))
#     time.sleep(1)
#     print("结束{}\n".format(name))

# if __name__ == "__main__": 
#     t1 = threading.Thread(target=test,args=("1",))
#     t2 = threading.Thread(target=test,args=("2",))

#     t1.start()
#     t2.start()
    
#     t1.join()
#     t2.join()
# print("over")
# if __name__ == "__main__": 
#       print("并发")
#       x = time.time()
    
#       T = Test("1")
#       S = Test("S")

#       T.start()
#       S.start()

#       T.join()
#       S.join()
#       y = time.time()
#       print(f"over:{y-x}")
#       print("串行")
#       x = time.time()
#       T = Test("11")
#       S = Test("SS")
#       T.run()
#       S.run()
#       y = time.time()
#       print(f"over:{y-x}")

import time 
import threading
from concurrent.futures import ThreadPoolExecutor

class Test(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print("开始{}\n".format( self.name))
        time.sleep(1)
        print("结束{}\n".format( self.name))

def test(name):
    print("开始{}\n".format(name))
    time.sleep(1)
    print("结束{}\n".format(name))

if __name__ == "__main__":
    print("串行开始")
    start = time.time()
    
    for i in range(10):
        test(i)
    over = time.time()
    print(f"耗时：{over-start}")

    print("并行开始")
    start = time.time()
    
    with ThreadPoolExecutor(max_workers= 10) as executor:

        executor.map(test,range(10))
    

    over = time.time()
    print(f"耗时：{over-start}")
