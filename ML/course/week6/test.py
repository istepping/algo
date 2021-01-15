from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

faces = fetch_lfw_people()
faces.data.shape,faces.images.shape