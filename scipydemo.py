import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fftpack import fft2
import time

moon=plt.imread('data/moonlanding.png')
plt.figure(figsize=(10,8))
plt.imshow(moon,cmap='gray')
plt.show()
