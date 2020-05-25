
import numpy as np 
import math 
import random
import matplotlib.pyplot as plt
import seaborn as sns 
from scipy.stats import norm


np.random.seed(3)
distribution = np.random.uniform(0,10,80000)
plt.title("Uniform Distribution")
plt.xlabel('Random Variables between 0 and 10')
plt.ylabel("Frequency")
plt.hist(distribution,edgecolor = 'black')
plt.show()
print('The population mean is: ',round(np.mean(distribution),6))



xbar = []
num_samples = 20000
n = 30
k = n
for i in range(0,num_samples): 
    sample = random.choices(distribution,k=n)
    avg = np.mean(sample)
    xbar.append(avg)
mu  = round(np.mean(xbar),6)
std = round(np.std(xbar),6)
print("The sample mean is equal to", mu,"with a standard deviation of",std ," when n =",n)



import pandas as pd
data = {'Sample size n':  [2,5,10,20,30],
       "Mean": [ 5.034652,5.011388,5.013351,5.016147,5.014476 ],
       "Standard deviation": [2.054247,1.289262,0.915367,0.641544,0.525793]}
df =pd.DataFrame(data, columns = ["Sample size n","Mean", "Standard deviation"],
                index = ['A', "B", 'C','D', "E"]) 
df



num_bins = 20
step = (max(xbar) - min (xbar))/ num_bins
num_classes = []
for q in range(0,num_bins):
    incr = min(xbar) + q*step
    num_classes.append(round(incr,1))



norm_xbar = np.linspace(min(xbar), max(xbar), num_samples)
plt.title("Sample Mean Distribution, n = 5")
plt.xlim(min(xbar),max(xbar))
plt.xlabel('Random Variables')
plt.ylabel("Density")
plt.hist(xbar, bins= num_classes, edgecolor = "black", align = "mid", density = True,color = "yellow")
plt.plot(norm_xbar,norm.pdf(norm_xbar,mu,std),linewidth=2, color = "b")







