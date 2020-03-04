# -*- coding: utf-8 -*-


from scipy.stats import poisson
import matplotlib.pyplot as plt
fig.ax=plt.subplot(1,1)
mu=0.0
mean,var,sken,kurt=poisson.stats(mu,moments='mvsk') 
x=np.arange(poisson.ppf(0.01,mu)),
 poisson.ppf(0.99,mu) 
ax.plot(x,poisson.pmf(x,mu),colors='b',lw=5,alpha=0.5)
      