#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


#read in the CSV data using Pandas
data = pd.read_csv("C:/Users/nicol/Uni 2019-2020/Python 2020/G2.Galaxy.Data.csv", delimiter = ',')

data_s = pd.read_csv("C:/Users/nicol/Uni 2019-2020/Python 2020/snapshots.milli.csv", delimiter=',',comment='#')


# In[198]:


#test new snapshot data table from Millennium Database
data_s[['snapNum','Z','lookbackTime']]

#each individual snapshot number has the same redshift value 


# In[10]:


#try to make  functions to translate between columns

def snaptoz(snapshots):
    """
    Given a snapshot column from a snapnum 
    Millennium Database column, return the 
    redshift values for that simulation in order.
    That is, in the order of the snapshot column.
    
    Note that the index and snapshot number in 
    the second Pandas dataframe are equivalent.
    
    For future databases, this may not be the case.
    Then, using the snapshot number from the main
    dataframe, you need to find the snapshot in the 
    second dataframe, and get the index number first
    before translating to the redshift values. 
    
    Also note that the second dataframe has more 
    decimal places in redshift values. 
    """
    #snapshots_values = snapshots.sort_values()
    z_list = []
    
    for snapshot in snapshots:
        z_list.append(data_s['Z'][snapshot])
    return z_list


# In[21]:


#test the values 
#snaptoz(data['snapnum'])

#data['redshift'] == snap_z(data['snapnum'])
#this will have False values because the databases have different decimal places 


# In[16]:


def snaptolookback(snapshots):
    """
    Given a snapshot number column from a snapnum 
    Millennium Database column, return the 
    lookbacktime column for that simulation in order.
    That is, in the order of the snapshot column.
    
    Note that the index and snapshot number in 
    the second Pandas database are equivalent.
    
    For future databases, this may not be the case.
    Then, using the snapshot number from the main
    database, you need to find the snapshot in the 
    second database, and get the index number first
    before translating to the lookbacktime values.
    """
    #snapshots_values = snapshots.sort_values()
    lookback_list = []
    
    for snapshot in snapshots:
        lookback_list.append(data_s['lookbackTime'][snapshot])
    return lookback_list


# In[22]:


#test
#snaptolookback(data['snapnum'])
#print(len(snaptolookback(data['snapnum'])))


# In[ ]:


"""
Things I've tried:
get limits of the redshift
this won't work since the list isn't linear! redshift[500] is like 4
I need the corresponding number for each snapshot value on left to display
on right hand side y-label
Or do we?
look at full snapnum and redshift columns to compare 
mini, maxi = data['redshift'][0], data['redshift'][999]

#ax2.set_ylim(maxi, mini)
#set_ylim does same thing as invert

"""


# In[110]:


#Improve Plots: redshift axis
#example: stellar mass
fig, ax1 = plt.subplots()

ax1.scatter(data['galaxyID'], data['snapnum'], data['stellarMass'], marker='.', c='black')
ax1.plot(data['descendantId'], data['snapnum'], linewidth=0.5)
ax1.set_title('MB G2 Galaxy Tree: Stellar Mass')
ax1.set_xlabel("galaxy ID")
ax1.set_ylabel("snapshot (62 is the root)", color='g')

#create second axis of redshift values
#need to remove the middle ticks but keep the end values for reference
ax2 = ax1.twinx()
ax2.set_ylim(10, 63)
ax2.set_yticks(data['snapnum'][::25])
ax2.set_yticklabels(snaptoz(data['snapnum'][::25]))
ax2.tick_params(axis='y', which='major', labelsize=5)
ax2.set_ylabel("redshift values", color='b', rotation='horizontal')
ax2.yaxis.set_label_coords(1.05,1.05)
plt.savefig("MDBG2.secondaxis.pdf", bbox_inches='tight')
plt.show()


# In[113]:


#try plotting with lookbacktime values 
#example: stellar mass
fig, ax1 = plt.subplots()

ax1.scatter(data['galaxyID'], data['snapnum'], data['stellarMass'], marker='.', c='black')
ax1.plot(data['descendantId'], data['snapnum'], linewidth=0.5)
ax1.set_title('MB G2 Galaxy Tree: Stellar Mass')
ax1.set_xlabel("galaxy ID")
ax1.set_ylabel("snapshot (62 is the root)", color='g')

#create second axis of redshift values
#need to remove the middle ticks but keep the end values for reference
ax2 = ax1.twinx()
ax2.set_ylim(0, 63)
ax2.set_yticks(data['snapnum'][::25])
ax2.set_yticklabels(snaptolookback(data['snapnum'][::25]))
ax2.tick_params(axis='y', which='major', labelsize=5)
ax2.set_ylabel("lookbacktime ($10^9$ years)", color='b', rotation='horizontal')
ax2.yaxis.set_label_coords(1.05,1.07)

#bbox_inches does not cut off the pdf
plt.savefig("MDBG2.lookbacksecond.pdf",bbox_inches='tight')
plt.show()                                                      


# In[37]:


#Display all of the rows of the following columns
pd.set_option('display.max_rows', None)
data[['snapnum', 'redshift']]


# In[73]:


#plotting using mass weighted age
plt.scatter(data['galaxyID'], data['snapnum'], data['massWeightedAge'], marker='.', c='black')
plt.plot(data['descendantId'], data['snapnum'], linewidth=0.5)
plt.title('MB G2 Galaxy Tree: Mass Weighted Age')
plt.xlabel("galaxy ID")
plt.ylabel("snapshot (62 is the root)")
#plt.savefig("MDBG2.Evolution2.pdf")
plt.show()


# In[72]:


plt.scatter(data['massWeightedAge'], data['sfr'], marker='.', c='black')
plt.title('MDB Age Vs. Star Formation Rate')
plt.xlabel("Mass Weighted Age (10^9 yr)")
plt.ylabel("Star Formation Rate (Msun/yr)")
#plt.savefig("MDBG2.Mass.SFR.pdf")
plt.show()


# In[54]:


#stellar mass
plt.scatter(data['massWeightedAge'], data['stellarMass'], marker='.', c='black')
plt.title('MDB Age Vs. Stellar Mass')
plt.xlabel("Mass Weighted Age (10^9 yr)")
plt.ylabel("Stellar Mass (10^10/h Msun)")
#plt.savefig("MDBG2.Mass.SFR.pdf")
plt.show()


# In[55]:


#stellar mass with parameters
plt.scatter(data['massWeightedAge'], data['stellarMass'], data['sfr'], marker='o', c='black')
plt.title('MDB Age Vs. Stellar Mass')
plt.xlabel("Mass Weighted Age (10^9 yr)")
plt.ylabel("Stellar Mass (10^10/h Msun)")
#plt.savefig("MDBG2.Mass.SFR.pdf")
plt.show()


# In[48]:


#ejected mass 
plt.scatter(data['massWeightedAge'], data['ejectedMass'], marker='.', c='black')
plt.title('MDB Age Vs. Ejected Mass')
plt.xlabel("Mass Weighted Age (10^9 yr)")
plt.ylabel("Ejected Mass (10^10/h Msun)")
#plt.savefig("MDBG2.Mass.SFR.pdf")
plt.show()


# In[57]:


#ejected mass 
plt.scatter(data['massWeightedAge'], data['coldGas'], data['sfr'], marker='.', c='black')
plt.title('MDB Age Vs. Cold Gas')
plt.xlabel("Mass Weighted Age (10^9 yr)")
plt.ylabel("Cold Gas (10^10/h Msun)")
#plt.savefig("MDBG2.Mass.SFR.pdf")
plt.show()


# In[64]:


#black hole mass 
plt.scatter(data['massWeightedAge'], data['blackHoleMass'],marker='.', c='black')
plt.title('MDB Age Vs. Mass of Central Black Hole')
plt.xlabel("Mass Weighted Age (10^9 yr)")
plt.ylabel("Black Hole Mass (10^10/h Msun)")
#plt.savefig("MDBG2.Mass.SFR.pdf")
plt.show()


# In[ ]:




