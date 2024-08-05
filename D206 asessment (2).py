#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Telecommunication-churn-project.-Description" data-toc-modified-id="Telecommunication-churn-project.-Description-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Telecommunication churn project. Description</a></span></li><li><span><a href="#Step-1.-Data-preprocessing" data-toc-modified-id="Step-1.-Data-preprocessing-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Step 1. Data preprocessing</a></span><ul class="toc-item"><li><span><a href="#Loading-the-data-and-studying-general-info" data-toc-modified-id="Loading-the-data-and-studying-general-info-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Loading the data and studying general info</a></span></li><li><span><a href="#Step-1:-Remove-irrelevant-data" data-toc-modified-id="Step-1:-Remove-irrelevant-data-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Step 1: Remove irrelevant data</a></span></li><li><span><a href="#Step-2:-Deduplicate-data" data-toc-modified-id="Step-2:-Deduplicate-data-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Step 2: Deduplicate data</a></span></li><li><span><a href="#Step-3:-Fix-structural-error-(Correcting-column-names,-types)" data-toc-modified-id="Step-3:-Fix-structural-error-(Correcting-column-names,-types)-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Step 3: Fix structural error (Correcting column names, types)</a></span></li><li><span><a href="#Step-3.-Deal-with-missing-data" data-toc-modified-id="Step-3.-Deal-with-missing-data-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Step 3. Deal with missing data</a></span></li><li><span><a href="#Outliers" data-toc-modified-id="Outliers-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Outliers</a></span></li><li><span><a href="#Data-wrangling" data-toc-modified-id="Data-wrangling-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Data wrangling</a></span></li><li><span><a href="#PCA" data-toc-modified-id="PCA-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>PCA</a></span></li></ul></li></ul></div>

# # Telecommunication churn project. Description

# The goal of this project is to clean data to prepare datasets for future analysis of churn rate of customers. One of hypotethical question could be which factors are the most important for customers who are staying with the company for a long time. Telecommunication company needs to update the strategy to retain existing customer as it is much cheaper than to attract a new one.

# # Step 1. Data preprocessing

# ## Loading the data and studying general info

# In[1]:


#import all packages 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().system('pip install missingno')
import missingno as msno
from sklearn.decomposition import PCA
import matplotlib.patches as mpatches
from matplotlib.cbook import boxplot_stats
import warnings
warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv('churn_raw_data.csv', error_bad_lines=False, sep = ',', engine = 'python')   


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


display(data.describe(include=["int", "float"]))
display(data.describe(include="object"))


# The data above help us to see that there are some missing data (we will calculate percentage below), incorrect datatypes which should be changed. To make dataset more readable we need to change column names and description to lowercase. 
# We can see also that the most often making order "white hanging heart t-light holder". 

# ## Step 1: Remove irrelevant data

# In[6]:


data=data.drop('ï»¿', axis=1)


# ## Step 2: Deduplicate data

# In[7]:


#checking if there are duplicates(False=no duplicates)
data.duplicated().value_counts()


# In[8]:


#Deleting duplicates 
#data = data.drop_duplicates().reset_index(drop = True)


# ## Step 3: Fix structural error (Correcting column names, types)

# In[9]:


# changing the register of letters in headers
data.columns = [x.lower() for x in data.columns]


# In[10]:


# renaming column names with underscores 
data.rename(columns = {'caseorder':'case_order', 'internetservice':'internet_service', 'onlinesecurity':'online_security', 'onlinebackup':'online_backup', 'deviceprotection':'device_protection', 'techsupport':'tech_support', 'streamingtv':'streaming_tv', 'streamingmovies':'streaming_movies','paperlessbilling':'paperless_billing', 'item1':'timely_response', 'item2':'timely_fixes', 'item3':'timely_replace', 'item4':'reliability', 'item5':'options', 'item6':'respect_response', 'item7':'courteous_exchange', 'item8':'active_listen', 'monthlycharge':'monthly_charge', 'paymentmethod':'payment_method'}, inplace = True)


# In[11]:


data.head()


# In[12]:


#data[['customer_id', 'interaction', 'city', 'state', 'county','zip', 'churn', 'techie', 'port_modem', 'tablet','phone', 'multiple', 'online_security','device_protection', 'tech_support', 'streaming_tv','streaming_movies', 'paperless_billing']] = data[['customer_id', 'interaction', 'city', 'state', 'county','zip', 'churn', 'techie', 'port_modem', 'tablet','phone', 'multiple', 'online_security','device_protection', 'tech_support', 'streaming_tv','streaming_movies', 'paperless_billing']].astype(str)


# In[13]:


data.columns


# In[14]:


data[['timely_response', 'timely_fixes','timely_replace', 'reliability', 'options', 'respect_response','courteous_exchange', 'active_listen']] = data[['timely_response', 'timely_fixes','timely_replace', 'reliability', 'options', 'respect_response','courteous_exchange', 'active_listen']].astype('category')


# In[15]:


#check if there are any incorrect names of unique data
data2=data[['payment_method', 'internet_service', 'contract', 'gender', 'marital', 'area', 'education']]
for col in data2.columns:
    print(data[col].unique())


# In[16]:


#check if there is any other unique names except yes or no
data3=data[['churn', 'techie', 'port_modem', 'tablet',
       'phone', 'multiple', 'online_security',
       'device_protection', 'tech_support', 'streaming_tv',
       'streaming_movies', 'paperless_billing']]
for col in data3.columns:
    
        print(data[col].unique())


# ## Step 3. Deal with missing data 

# In[17]:


#number of missing data
data.isnull().sum()


# In[18]:


#percentage of missing data in each column
for col in data.columns:
    pct_missing = np.mean(data[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# The code above was taken from https://proglib.io/p/moem-dataset-rukovodstvo-po-ochistke-dannyh-v-python-2020-03-27

# In[19]:


#dataset nans with missing data only
nans = data.loc[:, data.isnull().any()].copy()
nans


# Before deleting missing values completely, let's consider the factors for deletion, especially the size of the missing data. 
# Firstly I use msno.matrix() and msno.heatmap() to visualize missingness and the correlation between variables with missing data. It will help me determine pattern in missingness. Depending on the type of missingness I will take a decision about deleting missing data.

# In[20]:


msno.heatmap(nans,cmap="RdYlGn", figsize=(10,5), fontsize=12)


# Values close to 0, indicate there is little to no relationship between the presence of null values in one column compared to another.

# The code below is taken basen on the [2, 4] from list of resources.

# In[21]:


msno.matrix(data, sparkline=False, fontsize=12);
gray_patch = mpatches.Patch(color='gray', label='Data')
white_patch = mpatches.Patch(color='white', label='Missing data ')
plt.legend(handles=[gray_patch, white_patch])
plt.title('Missing data matrix')
plt.show()


# In[22]:


msno.matrix(data.sample(100), sparkline=False, fontsize=12);
gray_patch = mpatches.Patch(color='gray', label='Data')
white_patch = mpatches.Patch(color='white', label='Missing data ')
plt.legend(handles=[gray_patch, white_patch])
plt.title('Missing data matrix, labels are equivalent to the column name in dataset data')
plt.show()


# In[23]:


nans.hist(rwidth=1.0)
plt.tight_layout()


# In[24]:


#replacing Nans into median as histograms are right-skewed 
for col in data[['children', 'income', 'tenure', 'bandwidth_gb_year']]:
    data[col].fillna(data[col].median(), inplace=True)


# In[25]:


#replacing Nans into mean as histogram shows that data are spread more or less equally within whole range
data['age'].fillna(data['age'].mean(), inplace = True)


# In[26]:


for col in data[['techie', 'phone', 'tech_support']]:
    data[col].fillna(data[col].mode()[0], inplace=True)


# In[27]:


for col in data.columns:
    if data[col].isnull().sum()>0:
        print(data[col])


# ## Outliers

# In[28]:


data['children']=data['children'].astype(int)


# In[29]:


data1=data[['children','age','income','tenure','bandwidth_gb_year','monthly_charge', 'population']]
data1.columns


# In[30]:


data['lat'].max()


# In[31]:


data['lat'].min()


# In[32]:


data['lng'].max()


# In[33]:


data['lng'].min()


# In[34]:


#red_circle=dict(marketfacecolor='red', marker='o', markeredgecolor='white')

fig, axes = plt.subplots(1, len(data1.columns), figsize=(20,10))

for i, ax in enumerate(axes.flat):
    ax.boxplot(data1.iloc[:,i])
    ax.set_title(data1.columns[i], fontsize=20, fontweight='bold')
    ax.tick_params(axis='y', labelsize=14)

plt.tight_layout()


# The code below is taken from [7] list of resources.

# In[35]:



outliers_mc = boxplot_stats(data["monthly_charge"]).pop(0)['fliers']
res = data[~data["monthly_charge"].isin(outliers_mc)]


# In[36]:


outliers_ch = boxplot_stats(data["children"]).pop(0)['fliers']
res2 = res[~res["children"].isin(outliers_ch)]


# We can nottice that boxplot limit population around 300000 people and income around 75000$. But cutting down outliers with 75% threshold we will lost a lot of data. Lets have a look how data will changed if we put 99.9% threshold.

# In[37]:


# finding the 99.99 percentile thresholds
population_perc = np.percentile(data['population'], [99.99])[0]
print('99.9th percentile of population:', round(population_perc, 2))


# In[38]:


# finding the 99.99 percentile thresholds
income_perc = np.percentile(data['income'], [99.99])[0]
print('99.9th percentile of income:', round(income_perc, 2))


# In[39]:


clean_data=res2[(res2['population'] < population_perc)]


# In[40]:


clean_data=res2[(res2['income'] < income_perc)]


# In[41]:


clean_data.shape


# ## Data wrangling

# In[42]:


clean_data.info()


# In[43]:


cleaning_number=(len(data)-len(clean_data))/len(data)
print("Percentage of deleted data as outliers': {:.2%}".format(cleaning_number))


# In[44]:


# List of columns to be transformed
columns_to_change = ['churn', 'techie', 'port_modem', 'tablet',
       'phone', 'multiple', 'online_security',
       'device_protection', 'tech_support', 'streaming_tv',
       'streaming_movies', 'paperless_billing', 'online_backup']
clean_data[columns_to_change].head()


# In[45]:


# Define the mappings for each column
column_dict = {
    'churn_number': {'Yes': 1, 'No': 0},
    'techie_number': {'Yes': 1, 'No': 2},
    'port_modem_number': {'Yes': 1, 'No': 0},
    'tablet_number': {'Yes': 1, 'No': 0},
    'phone_number':{'Yes':1, 'No':0},
    'multiple_number':{'Yes':1, 'No':0},
    'online_security_number':{'Yes':1, 'No':0},
    'device_protection_number':{'Yes':1, 'No':0},
    'tech_support_number':{'Yes':1, 'No':0},
    'streaming_tv_number':{'Yes':1, 'No':0},
    'streaming_movies_number':{'Yes':1, 'No':0},
    'paperless_billing_number':{'Yes':1, 'No':0},
    'online_backup_number':{'Yes':1, 'No':0}
}
#clean_data[columns_to_change]=clean_data[columns_to_change].applymap(str)
new_columns=['churn_number', 'techie_number', 'port_modem_number', 'tablet_number',
       'phone_number', 'multiple_number', 'online_security_number',
       'device_protection_number', 'tech_support_number', 'streaming_tv_number',
       'streaming_movies_number', 'paperless_billing_number', 'online_backup_number']
clean_data[new_columns]=clean_data[columns_to_change]
clean_data.replace(column_dict, inplace=True)


# In[46]:


clean_data=clean_data.drop(columns_to_change, axis=1)


# In[47]:


clean_data.info()


# ## PCA

# In[48]:


pca_data=clean_data[['children', 'age', 'income', 'tenure', 'monthly_charge', 'bandwidth_gb_year']]


# In[49]:


#normalizing data
pca_data_normalized=(pca_data-pca_data.mean())/pca_data.std()


# In[50]:


pca=PCA(n_components=pca_data.shape[1])
#pca=PCA(n_components=0.85)
#pca.n_components
pca.fit(pca_data_normalized)


# The code below is taken from [2] List of resources

# In[51]:


pca_data2=pd.DataFrame(pca.transform(pca_data_normalized), columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6'])


# In[52]:


loadings=pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6'], index=pca_data_normalized.columns)
loadings


# In[53]:


cov_matrix=np.dot(pca_data_normalized.T, pca_data_normalized)/pca_data.shape[0]
eigenvalues=[np.dot(eigenvector.T, np.dot(cov_matrix, eigenvector)) for eigenvector in pca.components_]


# In[54]:


plt.plot(eigenvalues)
plt.xlabel('number of components')
plt.ylabel('eigenvalues')
plt.axhline(y=1, color='red')
plt.show()


# Eigenvalues gives information only about the individual variance of each component. Only cumulative variances could show an overview of the total variance explained as more components are included.

# In[55]:


pca = PCA()
pca.fit(pca_data_normalized)  # X represents your standardized dataset

# Sort the explained variances
explained_variances = pca.explained_variance_ratio_
sorted_variances = np.sort(explained_variances)[::-1]

# Calculate the cumulative explained variance
cumulative_variances = np.cumsum(sorted_variances)

# Plot the cumulative explained variance
plt.plot(range(1, len(cumulative_variances)+1), cumulative_variances, marker='o')
plt.xlabel('Number of components')
plt.ylabel('Cumulative variance')
plt.title('Cumulative variance')
plt.show()


# In[56]:


clean_data.to_csv('C:\учеба\WGU\D206\clean_data.csv', index=False)


# The list of resources:
# 1	Datacamp D206 – Data cleaning
# 2	WGU. D206. Webinars by Dr. Keoina Middleton
# 3	 https://towardsdatascience.com/how-to-select-the-best-number-of-principal-components-for-the-dataset-287e64b14c6d
# 4	https://coderzcolumn.com/tutorials/data-science/missingno-visualize-missing-data-in-python
# 5	https://medium.com/@brendaloznik_48450/pump-it-up-how-to-deal-with-missing-data-ac60178f1ae5 
# 6	https://towardsdatascience.com/create-and-customize-boxplots-with-pythons-matplotlib-to-get-lots-of-insights-from-your-data-d561c9883643
# 7	https://ru.stackoverflow.com/questions/1517587/%D0%9D%D0%B5-%D1%83%D0%B4%D0%B0%D0%BB%D1%8F%D1%8E%D1%82%D1%81%D1%8F-%D0%B2%D1%8B%D0%B1%D1%80%D0%BE%D1%81%D1%8B-%D0%B2-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B5-pandas
