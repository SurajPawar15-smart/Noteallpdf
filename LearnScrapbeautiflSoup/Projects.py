# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request,urlopen

req=Request('https://www.passportindex.org/byRank.php',headers={'User-Agent':'Mozilla/5.0'})
webpage=urlopen(req).read()

print(webpage)

soup=BeautifulSoup(webpage,'html')

country_name_html=[i for i in soup.find_all(class_='name_country')]

country_name=list()

for i in range(len(country_name_html)):
  country_name.append(country_name_html[i].text)

print(country_name)

VFS_html=[i for i in soup.find_all(class_='name_rank')]

VFS=list()

for i in range(len(VFS_html)):
  VFS.append(VFS_html[i].text)

print(VFS)

rank_vf_html=[i for i in soup.find_all(class_='rank vf')]
rank_vf=list()
for i in range(len(rank_vf_html)):
  rank_vf.append(rank_vf_html[i].text)

rank_voa_html=[i for i in soup.find_all(class_='rank voa')]
rank_voa=list()
for i in range(len(rank_voa_html)):
  rank_voa.append(rank_voa_html[i].text)

rank_vr_html=[i for i in soup.find_all(class_='rank vr')]
rank_vr=list()
for i in range(len(rank_vr_html)):
  rank_vr.append(rank_vr_html[i].text)

dict1={'country':country_name,'VFS':VFS,'rank_vf':rank_vf,'rank_voa':rank_voa,'rank_vr':rank_vr}

print(dict1)

df=pd.DataFrame.from_dict(dict1)

df.head()

df.tail()

