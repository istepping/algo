import random
import numpy as np;


def create_data(A, B, C, D, E, F, R):
    dataA = "%.2f" % (random.uniform(A[0], A[1]))
    dataB = "%.2f" % (random.uniform(B[0], B[1]))
    dataC = "%.2f" % (random.uniform(C[0], C[1]))
    dataD = "%.2f" % (random.uniform(D[0], D[1]))
    dataE = "%.2f" % (random.uniform(E[0], E[1]))
    dataF = "%.2f" % (random.uniform(F[0], F[1]))
    with open(r"data.txt", encoding='utf-8', mode='a') as f:
        f.write(dataA)
        f.write("\t")
        f.write(dataB)
        f.write("\t")
        f.write(dataC)
        f.write("\t")
        f.write(dataD)
        f.write("\t")
        f.write(dataE)
        f.write("\t")
        f.write(dataF)
        f.write("\t")
        f.write(R)
        f.write("\n")


for i in range(10000):
    create_data((0.4, 0.6), (0.1, 0.3), (0.1, 0.4), (0.1, 0.3), (0.4, 0.5), (0.0, 0.8), "1")
    create_data((0.0, 1.0), (0.5, 0.8), (0.0, 0.1), (0.2, 0.6), (0.0, 0.5), (0.0, 0.5), "3")
    create_data((0.4, 0.6), (0.2, 0.5), (0.7, 1.0), (0.1, 0.8), (0.2, 0.6), (0.5, 1.0), "4")
    if i % 2 == 0:
        create_data((0.0, 0.4), (0.8, 1.0), (0.1, 3.0), (0.5, 1.0), (0.0, 0.3), (0.0, 0.5), "2")
        create_data((0.3, 0.4), (0.0, 0.2), (0.6, 0.9), (0.1, 0.5), (0.7, 1.0), (0.6, 1.0), "5")
        create_data((0.3, 0.4), (0.0, 0.5), (0.5, 0.8), (0.0, 0.4), (0.3, 0.8), (0.8, 1.0), "6")
    else:
        create_data((0.6, 1.0), (0.8, 1.0), (0.1, 3.0), (0.5, 1.0), (0.0, 0.3), (0.0, 0.5), "2")
        create_data((0.6, 0.7), (0.0, 0.2), (0.6, 0.9), (0.1, 0.5), (0.7, 1.0), (0.6, 1.0), "5")
        create_data((0.6, 0.7), (0.0, 0.5), (0.5, 0.8), (0.0, 0.4), (0.3, 0.8), (0.8, 1.0), "6")
