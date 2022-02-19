#me auto to kommati sullegei ta stoixeia apo thn istoselida kai ta xrshmopoiei sthn sunexeia
from random import random
from re import A
import pandas as pd
from pandas import value_counts
from urllib.request import Request, urlopen
import numpy
from scipy.stats import entropy
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
#metatrepei to data se string
data = str(data)
#phgainei sth thesh pou brisketai o arithmos tou round
round=(data[11:18])
#kanei ton arithmo tou round apo string se akeraia timh
round = int(round)
randomness=(data[33:97])
#ekxwrei sto A tis randomness times
A=randomness

for i in range(19):
    #to round meiwnetai kata ena dioti theloume tis teleutaies 20 times
    round = round-1
                                                        #edw einai +str(round) gia na to parei sthn epanalupsh kai na to meiwsei opws sthn prohgoumenh grammh
    req = Request('https://drand.cloudflare.com/public/'+ str(round), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data = str(data)
    randomness=(data[33:97])
    #prosthetei kai tis kainourgies times randomnes mazi metis alles
    A = A + randomness

B = []
#ekxwrei kathe stoixeio tou A stin lista B
B[:0] = A
#me auto upologizetai h entropia to dekaeksadikou
pd_series = pd.Series(B)
counts = pd_series.value_counts()
entropy = entropy(counts)
print(entropy)