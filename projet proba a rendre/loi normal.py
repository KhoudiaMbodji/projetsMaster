# -*- coding: utf-8 -*-
"""Done By khoudia Mbodji MSDA option:IA"""
from scipy.stats import norm
norm.rvs()
import matplotlib.pyplot as plt
import numpy as np
abs=np.linspace(-5,5,200)
plt.plot(abs,norm.cdf(abs))
plt.grid()
plt.show()