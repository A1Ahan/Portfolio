#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('max_columns', 200)


# In[124]:


# DATA UNDERSTANDING

df = pd.read_csv("C:\\Users\\Jungs\Desktop\coaster_db.csv")
df


# In[125]:


df.shape


# In[126]:


df.head(20)


# In[127]:


df.columns


# In[128]:


df.dtypes


# In[129]:


df.describe()


# In[130]:


# DATA PREPARATION
df = df[['coaster_name', 
       #'Length', 'Speed',
       'Location', 'Status',
       # 'Opening date',
       # 'Type', 
       'Manufacturer', 
       # 'Height restriction', 'Model', 'Height',
       # 'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date', 
       #'Opened',
       # 'Replaced by', 'Website',
       # 'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       # 'Single rider line available', 'Restraint Style',
       # 'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean', 
       # 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 
         #'height_value', 'height_unit', 
       'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()


# In[131]:


df.shape


# In[132]:


pd.to_datetime(df['opening_date_clean'])


# In[133]:


# RENAMING COLUMNS

df = df.rename(columns={'coaster_name':'Coaster_Name',
                   'year_introduced':'Year_Introduced',
                   'opening_date_clean':'Opening_Date',
                   'speed_mph':'Speed_Mph',
                   'height_ft':'Height_ft',
                   'Inversions_clean':'Inversions',
                   'Gforce_clean':'Gforce'})


# In[134]:


df.head()


# In[135]:


df.isna().sum()


# In[136]:


df.loc[df.duplicated()]


# In[137]:


df.loc[df.duplicated(subset=['Coaster_Name'])].head(5)


# In[138]:


# CHECKING EXAMPLE OF DUPLICATE

df.query('Coaster_Name == "Crystal Beach Cyclone"')


# In[139]:


df.columns


# In[140]:


df = df.loc[~df.duplicated(subset=['Coaster_Name','Location','Opening_Date'])] .reset_index(drop=True).copy()
df


# In[141]:


df.shape


# In[142]:


# FEATURE UNDERSTANDING

df['Year_Introduced'].value_counts()


# In[154]:


ax =df['Year_Introduced'].value_counts()     .head(10)     .plot(kind='bar', title= 'Top Years Coasters Introduced')
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')


# In[155]:


df


# In[152]:


ax = df['Speed_Mph'].plot(kind='hist',
                         bins=20, title= 'Coaster Speed (mph)')

ax.set_xlabel('Speed (mph)')


# In[156]:


ax = df['Speed_Mph'].plot(kind='kde',
                         title= 'Coaster Speed (mph)')

ax.set_xlabel('Speed (mph)')


# In[157]:


# FEATURE RELATIONSHIPS

df


# In[164]:


df.plot(kind='scatter',
        x='Speed_Mph',
        y= 'Height_ft',
       title= 'Coaster Speed vs. Height')
plt.show()


# In[170]:


sns.scatterplot( x='Speed_Mph',
                y= 'Height_ft',
                hue= 'Year_Introduced',
                data= df)
plt.show()


# In[174]:


sns.pairplot(df, vars=['Year_Introduced', 'Speed_Mph', 'Height_ft', 'Inversions', 'Gforce'],
            hue= 'Type_Main')
plt.show()


# In[177]:


df_corr= df[['Year_Introduced', 'Speed_Mph', 'Height_ft', 'Inversions', 'Gforce']].dropna().corr()


# In[179]:


sns.heatmap(df_corr, annot=True)


# In[191]:


# ASKING QUESTIONS REGARDING WITH THE DATA

## Which locations have the fastest roller coasters? (Minimum of 10)?
df.query('Location != "Other"')     .groupby('Location')['Speed_Mph']     .agg(['mean','count'])     .query('count >= 10')     .sort_values('mean')     .plot(kind= 'barh', figsize=(12, 5), title = 'Average Coast Speed by Location')
ax.set_xlabel('Average Coaster Speed')
plt.show()


# In[185]:





# In[ ]:




