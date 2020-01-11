# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:49:30 2017

@author: Connor
"""

import pandas as pd
 
def moviesGrab_v2(yearStart, yearEnd):
        
    linkBase = r'https://www.boxofficemojo.com/year/'
    
    for year in range(yearStart, yearEnd+1):     
            
        dfsYear = pd.read_html(linkBase+str(year), header = 0)
        
        if year == yearStart:
            dfAll = dfsYear[0]
            dfAll['Year'] = [year] * len(dfAll)
        else:
            dfYear = dfsYear[0]
            dfYear['Year'] = [year] * len(dfYear)
            dfs = [dfAll, dfYear]
            
            dfAll = pd.concat(dfs, ignore_index = True)
        
    return(dfAll)

allYears = moviesGrab_v2(1977, 2019)

allYears.to_csv('all_year_boxoffice.csv', index=False)
