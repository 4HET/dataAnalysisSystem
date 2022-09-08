import pandas as pd


def df2xspreadsheetjson(df) -> str:
    cols = []
    # 重命名标题行，主要考虑标题行空等情况
    for col in df.columns:
        if col == "":
            cols.append(" ")  # 标题行空，一般不可能
        elif col is None:
            cols.append(" ")  # 表是空的
        else:
            cols.append(col)  # 复制过去
    # print(cols)
    df.columns = cols

    if df.shape[0] < 1 or df.shape[1] < 1:
        return '{}'
    metrics = cols
    df = df[metrics]  # 取我们需要的字段
    # 直接拼接字符串
    info = ''
    # 先拼接标题行
    info += '\"0\":{\"cells\":{'
    for i in range(len(metrics)):
        if i != len(metrics)-1:
            info += '\"' + str(i) + '\":' + '{\"text\":\"' + str(metrics[i]) + "\"},"
        else:
            info += '\"' + str(i) + '\":' + '{\"text\":\"' + str(metrics[i]) + "\"}"
    info += '}},'
    for index, row in df.iterrows():
        info += '\"'+str(index+1) + '\":'
        for j in range(len(metrics)):
            if j == 0:
                info += "{\"cells\":{"
            # print(row[col])
            if j != len(metrics)-1:
                info += '\"' + str(j)+'\":' + '{\"text\":\"' + str(row[metrics[j]]) + "\"},"
            else:
                info += '\"' + str(j) + '\":' + '{\"text\":\"' + str(row[metrics[j]]) + "\"}"
        info += '}},'

    rows = '{' + info + "\"len\":" + str(max(df.shape[0]+2, 50)) + '}'
    cols = 'cols\":{\"len\":' + str(df.shape[1]+1) + '}}'
    return rows




def file_to_json(file_id):
    df = pd.read_csv("DataAnalysis/per_data/{}.csv".format(file_id))
    s = df2xspreadsheetjson(df)
    # with open("dada.txt", "w", encoding="utf-8")as fi:
    #     fi.write(s)
    return s