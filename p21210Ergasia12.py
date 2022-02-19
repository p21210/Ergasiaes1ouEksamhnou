#me auto to kommati sullegei ta stoixeia apo thn istoselida kai ta xrshmopoiei sthn sunexeia
from random import random
from re import A
#import pandas as pd
#from pandas import value_counts
from urllib.request import Request, urlopen
import numpy
#from scipy.stats import entropy
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

for i in range(99):
    #to round meiwnetai kata ena dioti theloume tis teleutaies 20 times
    round = round-1
                                                        #edw einai +str(round) gia na to parei sthn epanalupsh kai na to meiwsei opws sthn prohgoumenh grammh
    req = Request('https://drand.cloudflare.com/public/'+ str(round), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data = str(data)
    randomness=(data[33:97])
    #prosthetei kai tis kainourgies times randomnes mazi metis alles
    A = A + randomness

end_length = len(A) * 4

A_as_int = int(A, 16)
A_bin = bin(A_as_int)
A_binary = A_bin[2:].zfill(end_length)

#print(A_binary)

A_bin0 = A_binary.replace("1"," ")
list = A_bin0.split(" ")
maxZeros= 0
for i in range(len(list)):
    if len(list[i])> maxZeros:
        maxZeros = len(list[i])
    
print("akolouthia mhdenikwn:", maxZeros)

A_bin1 = A_binary.replace("0"," ")
list = A_bin1.split(" ")
maxOnes= 0
for i in range(len(list)):
    if len(list[i])> maxOnes:
        maxOnes = len(list[i])
    
print("akolouthia monadwn:", maxOnes)