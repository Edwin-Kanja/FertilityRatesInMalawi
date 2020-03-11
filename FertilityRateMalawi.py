#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing required libraries for analysing data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[ ]:





# In[2]:


y=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/fertility-rates_national_mwi.csv")
y.head()


# In[3]:


#cheking whether there are any missing values
y.apply(lambda x:sum(x.isnull()), axis=0)


# In[ ]:





# In[4]:


A=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/iMPORTANT_COLUMNS.csv")
A


# # ASFR1992

# In[ ]:





# In[5]:


#ASFR for SurveyYear 1992
ASFR1992=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate 1992.csv")
ASFR1992


# In[6]:


m0=ASFR1992.mean().Value
m0


# In[ ]:





# In[7]:


#scatterplot-relationship for ASFR1992
plt.scatter(ASFR1992.Indicator, ASFR1992.Value, color="blue")
plt.title("Scatter Plot 1992 ASFR")
plt.xlabel('ASFR goup')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[8]:


#barchart-comparison for asfr1992
plt.bar(ASFR1992.Indicator, ASFR1992.Value, color="blue")
plt.title("BARCHART ASFR 1992")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[9]:


#line graph for ASFR 1992
plt.plot(ASFR1992.Indicator, ASFR1992.Value, color="blue")
plt.title("1992 ASFR TRENDS")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.show()


# In[ ]:





# # ASFR2000

# In[10]:


#ASFR for SurveyYear 2000
ASFR2000=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate 2000.csv")
ASFR2000


# In[11]:


m1=ASFR2000.mean().Value
m1


# In[12]:


#Scatter Plot relationship for 2000 ASFR
plt.scatter(ASFR2000.Indicator, ASFR2000.Value, color="green")
plt.title("Scatter Plot 2000 ASFR")
plt.xlabel('ASFRgroups')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[13]:


#barchart-comparison for asfr2000
plt.bar(ASFR2000.Indicator, ASFR2000.Value, color="green")
plt.title("BARCHART ASFR 2000")
plt.xlabel('ASFR groups')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[14]:


#line graph for ASFR 2000
plt.plot(ASFR2000.Indicator, ASFR2000.Value, color="green")
plt.title("2000 ASFR TRENDS")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.show()


# # ASFR 2004

# In[15]:


#ASFR for SurveyYear 2004
ASFR2004=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate 2004.csv")
ASFR2004


# In[16]:


m2=ASFR2004.mean().Value
m2


# In[17]:


#Scatter Plot-Relationship for 2004 ASFR
plt.scatter(ASFR2004.Indicator, ASFR2004.Value, color="red")
plt.title("Scatter Plot 2004 ASFR")
plt.xlabel('ASFR groups')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[18]:


#barchart-comparison for asfr2004
plt.bar(ASFR2004.Indicator, ASFR2004.Value, color="red")
plt.title("BARCHART ASFR 2004")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[19]:


#line graph for ASFR 2004
plt.plot(ASFR2004.Indicator, ASFR2004.Value, color="red")
plt.title("2004 ASFR TRENDS")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.show()


# # ASFR 2010

# In[20]:


#ASFR for SurveyYear 2010
ASFR2010=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate 2010.csv")
ASFR2010


# In[21]:


m3=ASFR2010.mean().Value
m3


# In[22]:


#Scatter Plot-Relationship for 2010 ASFR
plt.scatter(ASFR2010.Indicator, ASFR2010.Value, color="purple")
plt.title("Scatter Plot 2010 ASFR")
plt.xlabel('ASFR groups')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[23]:


#barchart-comparison for asfr2010
plt.bar(ASFR2010.Indicator, ASFR2010.Value, color="purple")
plt.title("BARCHART ASFR 2010")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[24]:


#line graph for ASFR 2010
plt.plot(ASFR2010.Indicator, ASFR2010.Value, color="purple")
plt.title("2010 ASFR TRENDS")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.show()


# # ASFR 2012

# In[25]:


#ASFR for SurveyYear 2012
ASFR2012=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate 2012.csv")
ASFR2012


# In[26]:


m4=ASFR2012.mean().Value
m4


# In[27]:


#Scatter Plot-Relationship for 2012 ASFR
plt.scatter(ASFR2012.Indicator, ASFR2012.Value, color="black")
plt.title("Scatter Plot 2012 ASFR")
plt.xlabel('ASFR groups')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[28]:


#barchart-comparison for asfr2012
plt.bar(ASFR2012.Indicator, ASFR2012.Value, color="black")
plt.title("BARCHART ASFR 2012")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[29]:


#line graph for ASFR 2012
plt.plot(ASFR2012.Indicator, ASFR2012.Value, color="black")
plt.title("2012 ASFR TRENDS")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.show()


# # ASFR 2014

# In[30]:


#ASFR for SurveyYear 2014
ASFR2014=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate 2014.csv")
ASFR2014


# In[31]:


m5=ASFR2014.mean().Value
m5


# In[32]:


#Scatter Plot-Relationship for 2014 ASFR
plt.scatter(ASFR2014.Indicator, ASFR2014.Value, color="violet")
plt.title("Scatter Plot 2014 ASFR")
plt.xlabel('ASFR groups')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[33]:


#barchart-comparison for asfr2014
plt.bar(ASFR2014.Indicator, ASFR2014.Value, color="violet")
plt.title("BARCHART ASFR 2014")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[34]:


#line graph for ASFR 2014
plt.plot(ASFR2014.Indicator, ASFR2014.Value, color="violet")
plt.title("2014 ASFR TRENDS")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.show()


# 
# # ASFR 2015

# In[35]:


#ASFR for SurveyYear 2015
ASFR2015=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate 2015.csv")
ASFR2015


# In[36]:


m6=ASFR2015.mean().Value
m6


# In[37]:


#Scatter Plot-Relationship for 2015 ASFR
plt.scatter(ASFR2015.Indicator, ASFR2015.Value, color="yellow")
plt.title("Scatter Plot 2015 ASFR")
plt.xlabel('ASFR groups')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[38]:


#barchart-comparison for asfr2015
plt.bar(ASFR2015.Indicator, ASFR2015.Value, color="yellow")
plt.title("BARCHART ASFR 2015")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[39]:


#line graph for ASFR 2015
plt.plot(ASFR2015.Indicator, ASFR2015.Value, color="yellow")
plt.title("2015 ASFR TRENDS")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.show()


# # ASFR 2017

# In[40]:


#ASFR for SurveyYear 2017
ASFR2017=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate 2017.csv")
ASFR2017


# In[41]:


m7=ASFR2017.mean().Value
m7


# In[42]:


#Scatter Plot-Relationship for 2017 ASFR
plt.scatter(ASFR2015.Indicator, ASFR2017.Value, color="orange")
plt.title("Scatter Plot 2017 ASFR")
plt.xlabel('ASFR groups')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[43]:


#barchart-comparison for asfr2017
plt.bar(ASFR2017.Indicator, ASFR2017.Value, color="orange")
plt.title("BARCHART ASFR 2017")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.legend('key')
plt.show() 


# In[44]:


#line graph for ASFR 2017
plt.plot(ASFR2017.Indicator, ASFR2017.Value, color="orange")
plt.title("2017 ASFR TRENDS")
plt.xlabel('ASFR groups')
plt.ylabel(' value')
plt.show()


# In[45]:


xx={'Years':[1992, 2000, 2004, 2010, 2012, 2014, 2015, 2017],'Means':[m0, m1, m2, m3, m4, m5, m6, m7]}
xx


# In[46]:


yy=pd.DataFrame(xx)
yy


# In[47]:


#Scatter Plot-Relationship for means per year
plt.scatter(yy.Years, yy.Means)
plt.title("Scatter Plot-ASFR Means/year")
plt.xlabel('Survey years')
plt.ylabel('Average ASFR')
plt.legend('key')
plt.show()


# In[48]:


#line graph for ASFR Means per year
plt.plot(yy.Years, yy.Means)
plt.title("Average Means per Year")
plt.xlabel('SUrveyYears')
plt.ylabel('Average ASFR')
plt.show()


# In[49]:


#barchart-comparison for means per year
plt.bar(yy.Years, yy.Means)
plt.title("BARCHART ASFR Means/year")
plt.xlabel('Surveyyears')
plt.ylabel(' average ASFR')
plt.legend('key')
plt.show() 


# # ASFR-group 15-19

# In[50]:


ASFR15_19=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate_ 15-19.csv")
ASFR15_19


# In[127]:


MG1=ASFR15_19.mean().Value
MG1


# In[51]:


sb.pairplot(ASFR15_19)


# In[52]:


#Scatter Plot-Relationship of group 15_19 for all years
plt.scatter(ASFR15_19.SurveyYear, ASFR15_19.Value, color="blue")
plt.title("Scatter Plot for group 15-19 for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[53]:


#barchart-comparison for group 15_19 for all years
plt.bar(ASFR15_19.SurveyYear, ASFR15_19.Value, color="blue")
plt.title("BARCHART for group 15-19 for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[54]:


#line graph for group 15_19 for all years
plt.plot(ASFR15_19.SurveyYear, ASFR15_19.Value, color="blue")
plt.title("ASFR 15-19 TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[55]:


#Histogram for ASFR 15-19 for all survey years
ASFR15_19['SurveyYear'].hist(bins=50)
plt.title("Value Histogram")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend('key')
plt.show()


# # ASFR-group 20-24

# In[56]:


ASFR20_24=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate_ 20-24.csv")
ASFR20_24


# In[126]:


MG2=ASFR20_24.mean().Value
MG2


# In[57]:


sb.pairplot(ASFR20_24)


# In[58]:


#Scatter Plot-Relationship of group 20_24 for all years
plt.scatter(ASFR20_24.SurveyYear, ASFR20_24.Value, color="green")
plt.title("Scatter Plot for group 20_24 for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[59]:


#barchart-comparison for group 20_24 for all years
plt.bar(ASFR20_24.SurveyYear, ASFR20_24.Value, color="green")
plt.title("BARCHART for group 20_24 for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[60]:


#line graph for group 20_24 for all years
plt.plot(ASFR20_24.SurveyYear, ASFR20_24.Value, color="green")
plt.title("ASFR 20_24 TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[61]:


#Histogram for ASFR 20_24 for all survey years
ASFR20_24['SurveyYear'].hist(bins=50)
plt.title("Value Histogram")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend('key')
plt.show()


# # ASFR-group 25-29

# In[62]:


ASFR25_29=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate_ 25-29.csv")
ASFR25_29


# In[125]:


MG3=ASFR25_29.mean().Value
MG3


# In[63]:


sb.pairplot(ASFR25_29)


# In[64]:


#Scatter Plot-Relationship of group 25_29 for all years
plt.scatter(ASFR25_29.SurveyYear, ASFR25_29.Value, color="red")
plt.title("Scatter Plot for group 25_29 for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[65]:


#barchart-comparison for group 25_29 for all years
plt.bar(ASFR25_29.SurveyYear, ASFR25_29.Value, color="red")
plt.title("BARCHART for group 25_29 for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[66]:


#line graph for group 25_29 for all years
plt.plot(ASFR25_29.SurveyYear, ASFR25_29.Value, color="red")
plt.title("ASFR 25_29 TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[67]:


#Histogram for ASFR 25_29 for all survey years
ASFR25_29['SurveyYear'].hist(bins=50)
plt.title("Value Histogram")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend('key')
plt.show()


# # ASFR-group 30-34

# In[68]:


ASFR30_34=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate_ 30-34.csv")
ASFR30_34


# In[124]:


MG4=ASFR30_34.mean().Value
MG4


# In[69]:


sb.pairplot(ASFR30_34)


# In[70]:


#Scatter Plot-Relationship of group 30_34 for all years
plt.scatter(ASFR30_34.SurveyYear, ASFR30_34.Value, color="black")
plt.title("Scatter Plot for group 30_34 for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[71]:


#barchart-comparison for group 30_34 for all years
plt.bar(ASFR30_34.SurveyYear, ASFR30_34.Value, color="red")
plt.title("BARCHART for group 30_34 for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[72]:


#line graph for group 30_34 for all years
plt.plot(ASFR30_34.SurveyYear, ASFR30_34.Value, color="black")
plt.title("ASFR 30_34 TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[73]:


#Histogram for ASFR 30_34 for all survey years
ASFR30_34['SurveyYear'].hist(bins=50)
plt.title("Value Histogram")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend('key')
plt.show()


# # ASFR-group 35-39

# In[74]:


ASFR35_39=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate_ 35-39.csv")
ASFR35_39


# In[123]:


MG5=ASFR35_39.mean().Value
MG5


# In[75]:


sb.pairplot(ASFR35_39)


# In[76]:


#Scatter Plot-Relationship of group 35_39 for all years
plt.scatter(ASFR35_39.SurveyYear, ASFR35_39.Value, color="yellow")
plt.title("Scatter Plot for group 35_39 for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[77]:


#barchart-comparison for group 35_39 for all years
plt.bar(ASFR35_39.SurveyYear, ASFR35_39.Value, color="yellow")
plt.title("BARCHART for group 35_39 for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[78]:


#line graph for group 35_39 for all years
plt.plot(ASFR35_39.SurveyYear, ASFR35_39.Value, color="yellow")
plt.title("ASFR 35_39 TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[79]:


#Histogram for ASFR 35_39 for all survey years
ASFR35_39['SurveyYear'].hist(bins=50)
plt.title("Value Histogram")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend('key')
plt.show()


# # ASFR-group 40-44

# In[80]:


ASFR40_44=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate_ 40-44.csv")
ASFR40_44


# In[122]:


MG6=ASFR40_44.mean().Value
MG6


# In[81]:


#Scatter Plot-Relationship of group 40_44 for all years
plt.scatter(ASFR40_44.SurveyYear, ASFR40_44.Value, color="orange")
plt.title("Scatter Plot for group 40_44 for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[82]:


#barchart-comparison for group 40_44 for all years
plt.bar(ASFR40_44.SurveyYear, ASFR40_44.Value, color="orange")
plt.title("BARCHART for group 40_44 for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[83]:


#line graph for group 40_44 for all years
plt.plot(ASFR40_44.SurveyYear, ASFR40_44.Value, color="orange")
plt.title("ASFR 40_44 TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[84]:


#Histogram for ASFR 40_44 for all survey years
ASFR40_44['SurveyYear'].hist(bins=50)
plt.title("Value Histogram")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend('key')
plt.show()


# # ASFR-group 45-49

# In[85]:


ASFR45_49=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Age specific fertility rate_ 45-49.csv")
ASFR45_49


# In[121]:


MG7=ASFR45_49.mean().Value
MG7


# In[86]:


sb.pairplot(ASFR45_49)


# In[87]:


#Scatter Plot-Relationship of group 45_49 for all years
plt.scatter(ASFR45_49.SurveyYear, ASFR45_49.Value, color="violet")
plt.title("Scatter Plot for group 45_49 for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[88]:


#barchart-comparison for group 45_49 for all years
plt.bar(ASFR45_49.SurveyYear, ASFR45_49.Value, color="violet")
plt.title("BARCHART for group 45_49 for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[89]:


#line graph for group 45_49 for all years
plt.plot(ASFR45_49.SurveyYear, ASFR45_49.Value, color="violet")
plt.title("ASFR 45_49 TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[90]:


#Histogram for ASFR 45_49 for all survey years
ASFR45_49['SurveyYear'].hist(bins=50)
plt.title("Value Histogram")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend('key')
plt.show()


# In[136]:


MG={'Age_Group':['15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49'],'Means':[MG1, MG2, MG3, MG4, MG5, MG6, MG7]}
MG


# In[137]:


MMG=pd.DataFrame(MG)
MMG


# In[145]:


#Scatter Plot-Relationship of means of ASFR age groups
plt.scatter(MMG.Age_Group, MMG.Means)
plt.title("Scatter Plot for means of ASFR age groups")
plt.xlabel('Age groups')
plt.ylabel('means')
plt.legend('key')
plt.show()


# In[143]:


#line graph for means of ASFR age groups
plt.plot(MMG.Age_Group, MMG.Means)
plt.title("Line graph for meansASFR age groups")
plt.xlabel('Age groups')
plt.ylabel('mean')
plt.show()


# In[141]:


#barchart-comparing means of ASFR age groups
plt.bar(MMG.Age_Group, MMG.Means)
plt.title("BARCHART means of ASFR-age groups")
plt.xlabel('AgeGroups')
plt.ylabel(' Mean')
plt.legend('key')
plt.show()


# # CRUDE BIRTH RATE

# Number of births which occured in a population in one calendar year/Mid year population of that year)*1000 

# In[91]:


CBR=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Crude birth rate.csv")
CBR


# In[92]:


sb.pairplot(CBR)


# In[93]:


CBR.describe().Value


# The average CRUDE BIRTH RATE for Malawi is 38.3125

# In[94]:


#Scatter Plot-Relationship btwn Crude birth rates
plt.scatter(CBR.SurveyYear, CBR.Value)
plt.title("Scatter Plot for CBR for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[95]:


#line graph forCrude birth rates for all years
plt.plot(CBR.SurveyYear, CBR.Value)
plt.title("Crude birth rates TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[96]:


#barchart-comparing Crude birth rates for all years
plt.bar(CBR.SurveyYear, CBR.Value)
plt.title("BARCHART for Crude birth rates for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# # GENERAL FERTILITY RATE

# In[97]:


GFR=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/General fertility rate.csv")
GFR


# In[98]:


sb.pairplot(GFR)


# In[99]:


#Scatter Plot-Relationship btwn general fertility rates
plt.scatter(GFR.SurveyYear, GFR.Value)
plt.title("Scatter Plot for GFR for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[100]:


#line graph for GENERAL FERTILITY rates for all years
plt.plot(GFR.SurveyYear, GFR.Value)
plt.title("General fertility rates TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[101]:


#barchart-comparing General fertility rates for all years
plt.bar(GFR.SurveyYear, GFR.Value)
plt.title("BARCHART for General fertility rates for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[102]:


GFR.describe().Value


# # TOTAL FERTILITY RATE 15-44

# In[103]:


TFR15_44=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Total fertility rate 15-44.csv")
TFR15_44


# In[146]:


TFR15_44.mean().Value


# In[104]:


sb.pairplot(TFR15_44)


# In[105]:


#Scatter Plot-Relationship btwn total fertility rates
plt.scatter(TFR15_44.SurveyYear, TFR15_44.Value)
plt.title("Scatter Plot for TFR for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[106]:


#line graph for Total FERTILITY rates for all years
plt.plot(TFR15_44.SurveyYear, TFR15_44.Value)
plt.title("Total fertility rates TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[107]:


#barchart-comparing Total fertility rates for all years
plt.bar(TFR15_44.SurveyYear, TFR15_44.Value)
plt.title("BARCHART for Total fertility rates for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# # TOTAL FERTILITY RATE 15-49

# In[108]:


TFR15_49=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Total fertility rate 15-49.csv")
TFR15_49


# In[148]:


TFR15_49.mean().Value


# In[109]:


sb.pairplot(TFR15_49)


# In[110]:


#Scatter Plot-Relationship btwnTotall fertility rates
plt.scatter(TFR15_49.SurveyYear, TFR15_49.Value)
plt.title("Scatter Plot for TFR15_49 for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[111]:


#line graph forTFR15_49 for all years
plt.plot(TFR15_49.SurveyYear, TFR15_49.Value)
plt.title("TFR15_49 TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[112]:


#barchart-comparing TFR15_49 for all years
plt.bar(TFR15_49.SurveyYear, TFR15_49.Value)
plt.title("BARCHART for TFR15_49 for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# # TOTAL WANTED FERTILITY RATE

# In[113]:


TWFR=pd.read_csv("C:/Users/admin/Desktop/FertilityMalawiProj/Total wanted fertility rate.csv")
TWFR


# In[147]:


TWFR.mean().Value


# In[114]:


sb.pairplot(TWFR)


# In[115]:


#Scatter Plot-Relationship btwn TWFR
plt.scatter(TWFR.SurveyYear, TWFR.Value)
plt.title("Scatter Plot forTWFR for all survey years")
plt.xlabel('Years')
plt.ylabel('value')
plt.legend('key')
plt.show()


# In[116]:


#line graph for TWFR for all years
plt.plot(TWFR.SurveyYear, TWFR.Value)
plt.title("TWFR TRENDS 1992-2017")
plt.xlabel('Years')
plt.ylabel('value')
plt.show()


# In[117]:


#barchart-comparing TWFR for all years
plt.bar(TWFR.SurveyYear, TWFR.Value)
plt.title("BARCHART for TWFR for all survey years")
plt.xlabel('Years')
plt.ylabel(' value')
plt.legend('key')
plt.show()


# In[118]:


# joining the Total fertility rates
X=pd.concat([TFR15_44, TFR15_49, TWFR])
X


# In[119]:


sb.pairplot(X)


# In[120]:


#filter record of 1992
filter1=X['SurveyYear']<=1992
#applying filter to dataframe
new1=X[filter1]
new1


# In[ ]:





# In[ ]:




