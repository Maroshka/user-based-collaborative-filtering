import pandas as pd 
from scipy.stats import *
from math import *
from simpearson import *
import operator

def top_matches(data,me,n=5, sim=sim_pearson):

	scores = [(other,sim(data,me, other)) for other in data.keys() if me!=other]
	scores = sorted(scores, key=operator.itemgetter(1))
	return scores[-n:]