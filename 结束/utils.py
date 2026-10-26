from operator import index
import csv,os
import os.path
from pathlib import Path
from shlex import join
import string

from pandas.core.reshape import encoding
from log import set_log
import pandas as pd
import  matplotlib.pyplot as plt

#目录
P = Path("E:/VS_tools/Project/Learn_python/结束/data/")
PR = Path("E:/VS_tools/Project/Learn_python/结束/data_deal/")
PO = Path("E:/VS_tools/Project/Learn_python/结束/output/")
#日志
Logg =  set_log()

data_columns = ["group","value1","value2","note"]

def read():
    Logg.info("准备开始读取data文件下的csv文件")
    file_name = []
    
    global P
    Logg.info("记录文件名字\n")
    for f in P.glob("*.csv"):
        file_name.append(f.name)

    Logg.debug(f"data下的文件：{file_name}")
    os.chdir(P)

    for fn in file_name:
       try :
           with open(fn,"r",encoding= "utf-8",newline="") as f:
                Logg.info(f"正在读取文件{f.name}内容")
                Logg.debug(f"========{f.name}========")
                reader = csv.reader(f)
                header = next(reader)
                Logg.debug(header)
                for i in reader :
                    Logg.debug(i)
                Logg.debug("=========================")  
        
       except StopIteration :
           Logg.warning(f"该文件{f.name}内容为空,跳过，执行下一步")


def deal_with(file_name):

       Logg.info(f"进入{P}中读取目标文件")
       
       try:

           df = pd.read_csv(P/file_name,encoding = "UTF-8")
           Logg.debug(f"读取的数据如下:\n==========={file_name}==========\n {df.to_string(index = False)}")
                     
           if (df["note"] == "wrong").any():
               Logg.error(f"文件{file_name}内容出现错误！！！")

           if df.isnull().any().any():

               Logg.info("数据中存在空值")
               Logg.debug(f"空值的个数：{df.isnull().sum().sum()}")
               Logg.info(f"读取的列名：{df.columns.tolist()}")
           
               for i in df.columns.tolist():  
                   if i in ("value1","value2"):
                       Logg.debug(f"使用列{i}的平均值对其的数据空值进行填写")
                       df[i] = df[i].fillna(df[i].mean())           
                                                            
                   else :
                       Logg.debug(f"该列{i}不属于数据缺失")

               Logg.debug(f"对文件{file_name}进行后保存，路径:{PR}")
               df.to_csv(PR/file_name,index = False,encoding = "UTF-8")



       except pd.errors.EmptyDataError:
           Logg.error(f"读取的文件{file_name}是空的！！！")
       except pd.errors.DataError:
           Logg.error(f"文件{file_name}的操作是错误的，str不能求和")

       
def merge_csv_josn():
    global PR,PO
    df_list = []
    f = "summary.csv"

    Logg.info(f"开始合并清洗后的数据集，存到output/{f}中")
    for i in PR.glob("*.csv"):
        df = pd.read_csv(i,encoding = "utf-8")       
        df_list.append(df)

    os.chdir(PO) 
    fun_filetest(f)

    try :
        merge_data = pd.concat(df_list,axis = 0 , ignore_index= False)      
        merge_data.to_csv(os.path.join(PO,f),encoding="utf-8",index = False)
        Logg.info(f"将{f}中的内容存成josn格式")
        merge_data.to_json(PO/"summary.json",orient= "records")
    except ValueError:
        Logg.error("文件夹下data_deal/没有文件！！！")
    return 


def fun_filetest(file_name:str)->str :
   
    if os.path.exists(file_name):
        Logg.warning(f"文件{file_name}存在，准备覆盖")
        os.remove(file_name)
        Logg.info(f"创建文件{file_name}")
        with open(file_name,mode = "w",encoding= "utf-8") as f:
            pass
    return
              
if __name__ == "__main__":
    read()
    
    for i in P.glob("*csv"):
        deal_with(i.name)

    merge_csv_josn()
