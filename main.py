import pandas as pd 
from scipy.stats import *
from simpearson import *
from simdistance import *
from matches import *
from recommend import *
import operator

data= {'Jill': {'Avenger: Age of Ultron': 7.0,'Django Unchained': 6.5,'Gone Girl': 9.0,'Kill the Messenger': 8.0},'Julia': {'Avenger: Age of Ultron': 10.0,'Django Unchained': 6.0,'Gone Girl': 6.5,'Kill the Messenger': 6.0,'Zoolander': 6.5},'Max': {'Avenger: Age of Ultron': 7.0,'Django Unchained': 7.0,'Gone Girl': 10.0,'Horrible Bosses 2': 6.0,'Kill the Messenger': 5.0,'Zoolander': 10.0},'Robert': {'Avenger: Age of Ultron': 8.0,'Django Unchained': 7.0,'Horrible Bosses 2': 5.0,'Kill the Messenger': 9.0,'Zoolander': 9.0},'Sam': {'Avenger: Age of Ultron': 10.0,'Django Unchained': 7.5,'Gone Girl': 6.0,'Horrible Bosses 2': 3.0,'Kill the Messenger': 5.5,'Zoolander': 7.0},'Toby': {'Avenger: Age of Ultron': 8.5,'Django Unchained': 9.0,'Zoolander': 2.0},'William': {'Avenger: Age of Ultron': 6.0,'Django Unchained': 8.0,'Gone Girl': 7.0,'Horrible Bosses 2': 4.0,'Kill the Messenger': 6.5,'Zoolander': 4.0}}
movies = []
for key in data.keys():
    movies = movies + data[key].keys()
movies = list(set(movies))

recommendations = recommend(data, movies, 'Sam', sim=sim_distance)
print max(recommendations, key=operator.itemgetter(1))[0]