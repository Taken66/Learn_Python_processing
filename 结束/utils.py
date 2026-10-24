
import csv,os
from pathlib import Path
from log import set_log

Logg =  set_log()

def read():
    Logg.info("准备开始读取data文件下的csv文件")
    file_name = []
    
    P = Path("E:/VS_tools/Project/Learn_python/结束/data/")
    Logg.info("记录文件名字\n")
    for f in P.glob("*.csv"):
        file_name.append(f.name)

    Logg.debug(f"data下的文件：{file_name}")
    os.chdir("结束/data")

    for i in file_name:
        with open(i,"r",encoding= "utf-8",newline="") as f:
            Logg.info(f"正在读取文件{i}内容")
            Logg.debug(f"========{i}========")
            reader = csv.reader(f)
            header = next(reader)
            Logg.debug(header)
            for i in reader :
                Logg.debug(i)
            Logg.debug("====================================================================")  
    Logg.debug("\n")
   
              
if __name__ == "__main__":
    read()
