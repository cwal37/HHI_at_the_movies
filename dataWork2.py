# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:16:01 2017

@author: Connor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

studioMap  = pd.read_csv(r"C:\Users\.3\Documents\GitHub\HHI_at_the_movies\studio_mapping.csv")
dfAll  = pd.read_csv(r"C:\Users\.3\Documents\GitHub\HHI_at_the_movies\all_years_box_office.csv")



uYears = list(set(dfAll['Year'].values))

studioDictNew = dict(zip(studioMap['Original_Studio'].values,
                      studioMap['New_Studio'].values))
studioDictMild = dict(zip(studioMap['Original_Studio'].values,
                      studioMap['Same_Name'].values))
studioDictDsFx= dict(zip(studioMap['Original_Studio'].values,
                      studioMap['Disney_Fox'].values))
studioDictDsS= dict(zip(studioMap['Original_Studio'].values,
                      studioMap['Disney_Sony'].values))
studioDictDsU= dict(zip(studioMap['Original_Studio'].values,
                      studioMap['Disney_Universal'].values))
studioDictDsW= dict(zip(studioMap['Original_Studio'].values,
                      studioMap['Disney_Warner'].values))

dfAll['Studio_Owner'] = [studioDictNew[x] for x in dfAll['Distributor'].values]
dfAll['Studio_Consld'] = [studioDictMild[x] for x in dfAll['Distributor'].values]
dfAll['Ds_Fx'] = [studioDictDsFx[x] for x in dfAll['Distributor'].values]
dfAll['Disney_Sony'] = [studioDictDsS[x] for x in dfAll['Distributor'].values]
dfAll['Disney_Universal'] = [studioDictDsU[x] for x in dfAll['Distributor'].values]
dfAll['Disney_Warner'] = [studioDictDsW[x] for x in dfAll['Distributor'].values]


dfAll = dfAll[dfAll['Distributor'] != '-']
dfAll = dfAll[dfAll['Year'] >= 1980]

def calc_hhi(df, col):
    
    uYears = list(set(df['Year'].values))
    results = []
    for year in uYears:
        dfYear = df[df['Year'] == year]
        studios = list(set(dfYear[col].values))
        yearSqSharess = []
        for studio in studios:
            dfStudioYear = dfYear[dfYear[col] == studio]
            studioTotal = np.sum(dfStudioYear['Total Gross'])
            allTotal = np.sum(dfYear['Total Gross'])
            pctStudio = (studioTotal/allTotal)*100
            yearSqSharess.append(pctStudio*pctStudio)
        yearHHI = np.sum(yearSqSharess)
        results.append([int(np.floor(year)), yearHHI])
    
    dfResults = pd.DataFrame(results, columns  = ['Year', 'HHI'])
    
    return(dfResults)

originalHHI = calc_hhi(dfAll, 'Distributor')
originalHHI.to_csv('originalHHI.csv')

mergedHHI = calc_hhi(dfAll, 'Studio_Owner')
mergedHHI.to_csv('mergedHHI.csv')

smallChangeHHI = calc_hhi(dfAll, 'Studio_Consld')
smallChangeHHI.to_csv('smallChangeHHI.csv')

dsFxHHI = calc_hhi(dfAll, 'Ds_Fx')
dsFxHHI.to_csv('Disney_Fox.csv')

dsSony = calc_hhi(dfAll, 'Disney_Sony')
dsSony.to_csv('Disney_Sony.csv')

dsU = calc_hhi(dfAll, 'Disney_Universal')
dsU.to_csv('Disney_Universal.csv')

dsW = calc_hhi(dfAll, 'Disney_Warner')
dsW.to_csv('Disney_Warner.csv')

plt.rcParams["figure.figsize"] = (12,8)
plt.rcParams["font.weight"] = 'bold'
plt.rcParams["font.size"] = 12
plt.gca().xaxis.grid(True)
ind = np.arange(0, len(originalHHI))

originalHHI = originalHHI.sort_values('Year', ascending= True)
mergedHHI = mergedHHI.sort_values('Year', ascending= True)
smallChangeHHI = smallChangeHHI.sort_values('Year', ascending= True)
dsFxHHI = dsFxHHI.sort_values('Year', ascending= True)
dsSony = dsSony.sort_values('Year', ascending= True)
dsU = dsU.sort_values('Year', ascending= True)
dsW = dsW.sort_values('Year', ascending= True)

#plt.plot(originalHHI['HHI'].values, label = 'As Listed', linewidth = 3,
#         marker = 'o', markersize=8)
plt.plot(mergedHHI['HHI'].values, label = 'True Owner', linewidth = 3,
         marker = 'o', markersize=8)
plt.plot(smallChangeHHI['HHI'].values, label = 'Small Consolidation', linewidth = 3,
         marker='o', markersize=8)
#plt.plot(dsFxHHI['HHI'].values, label = 'Disney Passes', linewidth = 3,
#         marker='o', markersize=8)
plt.plot(dsSony['HHI'].values, label = 'Disney Buys Sony', linewidth = 3,
         marker='o', markersize=8)
plt.plot(dsU['HHI'].values, label = 'Disney Buys Universal', linewidth = 3,
         marker='o', markersize=8)
plt.plot(dsW['HHI'].values, label = 'Disney Buys Warner', linewidth = 3,
         marker='o', markersize=8)

plt.xticks(ind, smallChangeHHI['Year'].values, rotation=45)
plt.ylabel('HHI Value')
plt.xlabel('Year')
plt.title('HHI for Ownership Scenarios using Box Office Gross (1980-2019)')
plt.tight_layout()
plt.legend(loc=2)



plt.savefig('final_results_v4.png', dpi=350)



#plt.show()
    
    

