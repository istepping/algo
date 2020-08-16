def calc_weight(input1, input2):
    result = list(map(lambda x, y: (float(x) + float(y)) / 2, input1, input2))
    return " ".join(str(i) for i in result)
