import data.consumerActionAnalysis.acton as action


def check1():
    file = 'CDNOW_master.txt'
    df = action.read_file(file)
    print(df.head(10))  # 读取前10行,默认5行
    print(df.describe())
    # count(计数),mean(平均值),std(标准差),
    print(df.info())
    print(action.convert_time(df))
    action.analysis(df)
check1()
