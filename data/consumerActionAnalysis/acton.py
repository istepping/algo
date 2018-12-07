import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")  # 自带的美化方式


# 读取数据模块
def read_file(file):
    columns=['user_id','order_dt','order_projects','order_amount']
    # 文件名,列名,区分方式:1或多个空格
    df=pd.read_csv(file,names=columns,sep="\s+")
    return df