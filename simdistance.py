import pandas as pd 
from scipy.stats import *
from math import *

def sim_distance(data, user1, user2):
	si={}
	for item in data[user1]:
		if item in data[user2]:
			si[item]=1
	# if they have no ratings in common, return 0
	if len(si)==0: return 0
	# Add up the squares of all the differences
	sum_of_squares = sum([pow(data[user1][item] - data[user2][item],2) for item in si])
	return 1/(1+sum_of_squares)