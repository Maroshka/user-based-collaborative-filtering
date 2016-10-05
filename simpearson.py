import pandas as pd 
from scipy.stats import *

def sim_pearson(data,user1, user2):
    outdata = []
    for i in data[user1]:
        if i in data[user2]:
            outdata.append((i, data[user1][i], data[user2][i]))
          
    df = pd.DataFrame(data = outdata, columns=['movie', user1, user2])
    return pearsonr(df[user1], df[user2])[0]