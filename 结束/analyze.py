import logging
from os import path
from pathlib import Path
import pandas as pd
import  matplotlib.pyplot as plt
import os
from pandas.core.reshape import encoding
from log import set_log


Logg = set_log()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


P = Path(r"E:\VS_tools\Project\Learn_python\结束\output")
try :
    Logg.info("开始读取文件内容")
    df =  pd.read_csv(os.path.join(P,"summary.csv"),encoding = "utf-8" )
    print(df)
    print(df.info())

    df.plot()
    plt.show()
except FileNotFoundError :
    Logg.error("文件未查询到！！！,请检查前面的数据是否保存成功！！")
