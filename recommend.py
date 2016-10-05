import pandas as pd 
from scipy.stats import *
from simpearson import *
from simdistance import *
from matches import *
import operator

def recommend(data, movies, user, sim):
	scores = top_matches(data, user, 3, sim=sim)
	df2 = pd.DataFrame(data=scores, columns=['User','Sim'])
	# df2['test'] = [i for i in range(0, len(df2))]
	total = []
	simSum = []
	ratio = []
	for i in movies:
		l = []
		for k in df2['User']:
			if i in data[k].keys():
				l.append(data[k][i])
			else: 
				l.append(0)
		df2[i] = l
		total.append(sum(df2['Sim']*df2[i]))
		tmp = (df2[i] != 0)
		simSum.append(sum(df2['Sim']*(df2[i] != 0)))
		ratio.append((i,total[-1]/simSum[-1]))

	return ratio