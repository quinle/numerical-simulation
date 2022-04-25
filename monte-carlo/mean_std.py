# Let X~e^Z/sqrt(e) where Z~N(0,1). NOte that E[X] = 1.
# We find frequency with confidence interval contains exact mean

from random import seed
from random import random
import numpy as np
seed(1)
se = np.sqrt(np.exp(1))

M = 10^4
repeats = [10^2, 10^3, 10^4]
len = len(repeats)
m = [0]*len
s_mean = [0]*len
s_std = [0]*len

for i in range (0,(len-1)):
    reps = repeats[i]
    hits = 0
    for k in range (reps) :
        x = []
        for l in range (M):
            x.append(np.exp(np.random.normal())/se)
        s_mean = np.mean(x)
        s_std = np.std(x)
        ebar = 1.96*s_std/np.sqrt(M)
        clower = s_mean-ebar
        cupper = s_mean+ebar
        if s_mean - ebar < 1 and s_mean+ebar>1:
            hits = hits+1
    freq = hits/reps

print('frequencies = ')
print(freq)
