import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")  # 自带的美化方式


# 读取数据模块
def read_file(file):
    columns = ['user_id', 'order_dt', 'order_products', 'order_amount']
    # 文件名,列名,区分方式:1或多个空格
    df = pd.read_csv(file, names=columns, sep="\s+")
    return df


# 处理日期
def convert_time(df):
    df['order_date'] = pd.to_datetime(df.order_dt, format="%Y%m%d")
    df['month'] = df.order_date.values.astype('datetime64[M]')
    # 1009-01-02 12:20:30 %Y-1997 %y-97 %m-01 % d-02 %h-12 %M(分)-20 %s-30
    return df


# 1 分析每个月的销售量
def convert_dimension_month_order_products(df):
    # 月总销售量
    # groupby():分组函数
    grouped_month_order_products = df.groupby('month').order_products.sum()
    grouped_month_order_products.plot()
    plt.show()


# 2 分析每个月的销售额
def convert_dimension_month_order_amount(df):
    grouped_month_order_amount = df.groupby('month').order_amount.sum()
    grouped_month_order_amount.plot()
    plt.show()


# 3 用户分组
def convert_dimension_user_id(df):
    grouped_user_id = df.groupby('user_id')  # 数据维度转换为用户
    grouped_user_id_sum = grouped_user_id.sum()
    grouped_user_id_sum.plot.scatter(x='order_amount', y='order_products')  # 从用户ID的角度，画销售额和销量的散点图
    grouped_user_id.order_products.sum().hist(bins=30) #销售额和销量的直方图
    df.order_amount.hist(bins=30)  # 直方图，分层30组
    plt.show()
    grouped_user_id_month_min = grouped_user_id.month.min().value_counts()
    grouped_user_id_month_max = grouped_user_id.month.max().value_counts()

# 用户复购率
def repeat_purchase_ratio(df):
    pivoted_counts = df.pivot_table(index = 'user_id', columns = 'month',
                                    values='order_dt',aggfunc= 'count').fillna(0) #数据透视(用户每月的订单数)
    columns_month = df.month.sort_values().astype('str').unique()  #优化时间格式
    pivoted_counts.columns = columns_month
    pivoted_counts_transf = pivoted_counts.applymap(lambda x: 1 if x > 1 else np.NaN if x == 0 else 0)  # 转换数据格式，方便计算
    rep_purchase_ratio = (pivoted_counts_transf.sum() / pivoted_counts_transf.count())  # 复购率
    rep_purchase_ratio.plot(figsize=(10, 4))  # 复购率可视化
# 数据分析
def analysis(df):
    convert_dimension_month_order_products(df)
    convert_dimension_month_order_amount(df)
    convert_dimension_user_id(df)
    #repeat_purchase_ratio(df)
