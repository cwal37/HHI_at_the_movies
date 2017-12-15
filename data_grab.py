# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:49:30 2017

@author: Connor
"""

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import time, os, random, pdb
 

yearsRef = pd.read_csv(r'years_table.csv')

yearsDict = dict(zip(yearsRef['Year'].values, yearsRef['# of'].values))
colNames = ['Rank', 'Movie', 'Studio', 'Total Gross', 'All Theaters',
               'Opening Total', 'Opening Theaters', 'Open Date', 'Close Date', 'Year']

def moviesGrab(yearsDict):
        
    linkBase = r'http://www.boxofficemojo.com/yearly/chart/?page='
    linkSec = r'&view=releasedate&view2=domestic&yr='
    
    for year in yearsDict:     
            
        pages = int(np.floor(yearsDict[year]/100))        
        print(year)
        for page in range (1,pages+1):
            #print(page)
            try:
                totalURL = linkBase+str(page)+linkSec+str(year)+'&p=.htm'
                
                dfPage = pd.read_html(totalURL, skiprows=6, header=None)[2][:-6]
                
                if year < 2002:
                    dfPage[len(dfPage.columns)] = 0
                
                dfPage[len(dfPage.columns)] = year
                    
                dfPage.columns = colNames
                
                dfPage.to_csv(r'data_holding\page_'+str(page)+'_year_'+str(year)+'.csv')
                time.sleep(2)
            except IndexError:
                print('Records Incomplete')

moviesGrab(yearsDict)
