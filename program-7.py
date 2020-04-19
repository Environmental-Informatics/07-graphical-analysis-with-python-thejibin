# -*- coding: utf-8 -*-
"""
Created on 2020-04-14
by Jibin Joseph -joseph57

Assignment 07 - Graphical Analysis with Python

This program reads the earthquake data contained in a csv file for the data "30 days"
using pandas dataframe
Further, a Graphical Analysis with Python is performed on the data

Revision 02-2020-04-18
Modified to add comments
"""

## Import the required packages
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

## Read the csv data using pandas read.table() and printing the information of fields
eq_data=pd.read_table("all_month.csv",sep=',',header=0)
#eq_data.info()

## Generate a histogram of earthquake magnitude, using a bin width of 1 and a 
## range of 0 to 10
plt.figure(1,figsize=(11.69,8.27)) ## Create A4 size
range_start=0
range_end=10
binwidth=1
plt.hist(eq_data['mag'].dropna().values,bins=range(range_start,range_end+1,binwidth))
plt.title("Histrogram Plot of Earthquake Magnitude\n(binwidth="+str(binwidth)+
                                                     ",  range="+str(range_start)+" - "+
                                                     str(range_end)+")",fontsize=20)
plt.xlabel("Earthquake Magnitude",fontsize=15)
plt.ylabel("Frequency",fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(range(range_start,range_end+1,binwidth),fontsize=15)
plt.savefig("01_Histogram.png")
plt.close(1)

## Generate a KDE plot for the same data.
plt.figure(2,figsize=(11.69,8.27))
fig,ax1=plt.subplots()
ax1.set_xlabel("Earthquake Magnitude",fontsize=15)
ax1.set_ylabel("Density",fontsize=15)
eq_data['mag'].plot(kind='kde')
ax2=ax1.twinx() ## Create a second axes that share the same x-axis
ax2.set_ylabel("Frequency",fontsize=15)
eq_data['mag'].plot(kind='hist',bins=range(range_start,range_end+1,binwidth))
plt.title("KDE Plot of Earthquake Magnitude with Histogram\n\
          (kernel width= scott, kernel = Gaussian)\n \
          (hist binwidth="+str(binwidth)+", range= full)",fontsize=15)
fig.tight_layout()
plt.savefig("02_KDEPlot.png")
plt.close('all')

## Plot latitude versus longitude for all earthquakes. 
plt.figure(3,figsize=(11.69,8.27))
plt.scatter(eq_data['longitude'],eq_data['latitude'],marker='*')
plt.title("Scatter Plot of Earthquake Locations",fontsize=20)
plt.xlabel("Longitude (in dd)",fontsize=15)
plt.ylabel("Latitude (in dd)",fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.savefig("03_EarthquakeLocations_Lat_Lon.png")
plt.close(3)

## Generate a normalized cumulative distribution plot of earthquake depths.
plt.figure(4,figsize=(11.69,8.27))
binsize=500
plt.hist(eq_data['depth'].dropna().values,bins=binsize,cumulative=True,histtype="step",density=True,label='Empirical')
plt.title("Normalized CDF of Earthquake Depths\n(bins = "+str(binsize)+")",fontsize=20)
plt.xlabel('Depth (in km)',fontsize=15)
plt.ylabel("Density",fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.xlim(0,eq_data['depth'].max()-1) ## -1 will remove the vertical line
plt.legend(loc='lower right',frameon=True,fontsize=10)
plt.savefig("04_CDF.png")
plt.close(4)

## Generate a normalized cumulative distribution plot of earthquake depths.
plt.figure(5,figsize=(11.69,8.27))
plt.scatter(eq_data['mag'],eq_data['depth'],label='Depth-Magnitude')
plt.title("Scatter Plot of Depth vs Magnitude",fontsize=20)
plt.xlabel("Magnitude",fontsize=15)
plt.ylabel("Depth (in km)",fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
#plt.xlim(0,eq_data['depth'].max()-1) ## -1 will remove the vertical line
plt.legend(loc='lower right',frameon=True,fontsize=10)
plt.savefig("05_Scatter_Depth_Magnitude.png")
plt.close(5)

## Create a subset of eq data with mag >0
eq_data2=eq_data[eq_data['mag']>0]
#print(eq_data2)
#print("MIN",eq_data2['mag'].min())
#print("MAX",eq_data2['mag'].max())

## Generate a quantile or Q-Q plot of the earthquake magnitudes.
## Create 6 subplots with different distributions
plt.figure(6,figsize=(8.27,11.69))
plt.subplot(321)
stats.probplot(eq_data2['mag'].dropna().values,dist="uniform",plot=plt)
plt.title("Uniform Distribution")
plt.ylim(-2,10)

plt.subplot(322)
stats.probplot(eq_data2['mag'].dropna().values,dist="norm",plot=plt)
plt.title("Normal Distribution")
plt.ylim(-2,10)

plt.subplot(323)
stats.probplot(eq_data2['mag'].dropna().values,dist="gumbel_l",plot=plt)
plt.title("Gumbel Left Skewed")
plt.ylim(-2,10)

plt.subplot(324)
stats.probplot(eq_data2['mag'].dropna().values,dist="gumbel_r",plot=plt)
plt.title("Gumbel Right Skewed")
plt.ylim(-2,10)

plt.subplot(325)
lognorm_params=stats.lognorm.fit(eq_data2['mag'].dropna().values)
stats.probplot(eq_data2['mag'].dropna().values,fit=True,dist="lognorm",sparams=lognorm_params,plot=plt)
plt.title("Log Normal Distribution")
plt.ylim(-2,10)

plt.subplot(326)
pareto_params=stats.pareto.fit(eq_data2['mag'].dropna().values)
print(pareto_params)
stats.probplot(eq_data2['mag'].dropna().values,fit=True,dist="pareto",sparams=pareto_params,plot=plt)
plt.title("Pareto Distribution")
plt.ylim(-2,10)

plt.subplots_adjust(wspace=0.5)
plt.subplots_adjust(hspace=0.5)

plt.suptitle("QQ Plot of Earthquake Magnitude\n(Assuming Different Distribution)",fontsize=18)
plt.savefig("06_QQ_Plot_Magnitude.png")
plt.close(5)

"""
## Effect of binwidth and range
plt.figure(10)
plt.subplot(121)
range_start=0
range_end=10
binwidth=1
plt.hist(eq_data['mag'].dropna().values,bins=range(range_start,range_end+1,binwidth))
plt.title("Histrogram Plot of Earthquake Magnitude\n(binwidth="+str(binwidth)+
                                                     ",  range="+str(range_start)+" - "+
                                                     str(range_end)+")",fontsize=8)
plt.xlabel("Earthquake Magnitude",fontsize=8)
plt.ylabel("Frequency",fontsize=8)
plt.yticks(fontsize=8)
plt.xticks(range(range_start,range_end+1,binwidth),fontsize=8)

plt.subplot(122)
range_start=0
range_end=20
binwidth=1
plt.hist(eq_data['mag'].dropna().values,bins=range(range_start,range_end+1,binwidth))
plt.title("Histrogram Plot of Earthquake Magnitude\n(binwidth="+str(binwidth)+
                                                     ",  range="+str(range_start)+" - "+
                                                     str(range_end)+")",fontsize=8)
plt.xlabel("Earthquake Magnitude",fontsize=8)
plt.ylabel("Frequency",fontsize=8)
plt.yticks(fontsize=8)
plt.xticks(range(range_start,range_end+1,binwidth),fontsize=8)
plt.subplots_adjust(wspace=0.5)
plt.savefig("01_Histogram_binwdith.png")
plt.close(10)
"""