# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:16:01 2017

@author: Connor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#from file_walk_with_me import file_walk
#
#
#allDataList = file_walk(r'data_holding\\')
#
#for file in allDataList:
#    
#    df = pd.read_csv(r'data_holding\\'+file, encoding = 'ISO-8859-1', ignore_index = True)
#    
#    if file == allDataList[0]:
#        dfAll = df
#    else:
#        dfs = [dfAll, df]
#        dfAll = pd.concat(dfs, ignore_index = True)
#dfAll.to_csv(r'final_annual_data.csv')
#dfAll = pd.read_csv(r'final_annual_data.csv', encoding = 'ISO-8859-1')
#
#studiosTable = pd.read_csv(r'studios_table_merger.csv', encoding = 'ISO-8859-1')   
#
#
#studioDict = dict(zip(studiosTable['Abbrev'].values, studiosTable['Studio'].values))
#allAbbrevs = list(dfAll['Studio'].values)
#
#realStudio = []
#for studio in allAbbrevs:
#    try:
#        realStudio.append(studioDict[studio])
#    except KeyError:
#        realStudio.append('not mapped')
#    
#    
#dfAll['Studio Name'] = realStudio   
#
#dfMapped = dfAll[dfAll['Studio Name'] != 'not mapped'] 
#
#
#dfYears = dfAll[dfAll['Year'] > 1998]
#dfYears = dfYears[dfYears['Year'] != 2017]
#
#uYears = list(set(dfYears['Year'].values))
#
#
#results = []
#
#for year in uYears:
#    dfYear = dfYears[dfYears['Year'] == year]
#    studios = list(set(dfYear['Studio Name'].values))
#    yearSqSharess = []
#    for studio in studios:
#        dfStudioYear = dfYear[dfYear['Studio Name'] == studio]
#        studioTotal = np.sum(dfStudioYear['Total Gross'])
#        allTotal = np.sum(dfYear['Total Gross'])
#        pctStudio = (studioTotal/allTotal)*100
#        yearSqSharess.append(pctStudio*pctStudio)
#    yearHHI = np.sum(yearSqSharess)
#    results.append([int(np.floor(year)), yearHHI])
#    
#dfResults = pd.DataFrame(results, columns  = ['Year', 'HHI'])
#
#dfResults.to_csv('final_results_together.csv')
plt.rcParams["figure.figsize"] = (12,8)
dfSeparate = pd.read_csv(r'final_results_separate.csv')
dfMerger = pd.read_csv('final_results_together.csv')
ind = np.arange(0, len(dfMerger))
dfSeparate = dfSeparate.sort_values('Year', ascending= True)
dfMerger = dfMerger.sort_values('Year', ascending= True)
plt.plot(dfSeparate['HHI'].values, label = 'No Merger', linewidth = 3,
         marker = 'o', markersize=8)
plt.plot(dfMerger['HHI'].values, label = 'Disney Owns Fox', linewidth = 3,
         marker='o', markersize=8)
plt.xticks(ind, dfMerger['Year'].values)
plt.ylabel('HHI Value')
plt.xlabel('Year')
plt.title('HHI for Merger Scenarios using Box Office Gross (1999-2016)')
plt.tight_layout()
plt.legend(loc=2)

plt.savefig('final_results.png', dpi=350)



#plt.show()
    
    

