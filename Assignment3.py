#!/usr/bin/env python
# coding: utf-8

# In[97]:


import pandas as pd
import statistics as st
nd = pd.read_csv("listings.csv")
nd['reviews_per_month'].fillna(0, inplace = True)
print(nd.head())


# In[103]:


# discrete random variables:
#     price
#     minimum_nights
#     number_of_reviews
#     calculated_host_listings_count
#     availability_365

# print('Price:', nd['price'].isna().values.any())
# print('Minimum Nights:', nd['minimum_nights'].isna().values.any())
# print('Number of Reviews:', nd['number_of_reviews'].isna().values.any())
# print('Calculated Host Listings Count:', nd['calculated_host_listings_count'].isna().values.any())
# print('Availability 365:', nd['availability_365'].isna().values.any())

# continuous random variables:
#     latitude
#     longitude
#     reviews_per_month

# print('latitude:', nd['latitude'].isna().values.any())
# print('longitude:', nd['longitude'].isna().values.any())
# print('Reviews per Month:', nd['reviews_per_month'].isna().values.any())


# In[99]:


# Mean of discrete variables
print('Mean of:')
print('Price: {:.3f}' .format(nd['price'].mean()))
print('Minimum Nights: {:.3f}' .format(nd['minimum_nights'].mean()))
print('Number of Reviews: {:.3f}' .format(nd['number_of_reviews'].mean()))
print('Calculated Host Listings Count: {:.3f}' .format(nd['calculated_host_listings_count'].mean()))
print('Availability 365: {:.3f}' .format(nd['availability_365'].mean()))


# In[100]:


# Variance of discrete variables
print('Variance of:')
print('Price: {:.3f}' .format(st.variance(nd['price'])))
print('Minimum Nights: {:.3f}' .format(st.variance(nd['minimum_nights'])))
print('Number of Reviews: {:.3f}' .format(st.variance(nd['number_of_reviews'])))
print('Calculated Host Listings Count: {:.3f}' .format(st.variance(nd['calculated_host_listings_count'])))
print('Availability 365: {:.3f}' .format(st.variance(nd['availability_365'])))


# In[101]:


# Mean of continuous variables
print('Mean of:')
print('latitude: {:.3f}' .format(nd['latitude'].mean()))
print('longitude: {:.3f}' .format(nd['longitude'].mean()))
print('Reviews per Month: {:.3f}' .format(nd['reviews_per_month'].mean()))


# In[102]:


# Variance of continuous variables
print('Variance of:')
print('latitude: {:.3f}' .format(st.variance(nd['latitude'])))
print('longitude: {:.3f}' .format(st.variance(nd['longitude'])))
print('Reviews per Month: {:.3f}' .format(st.variance(nd['reviews_per_month'])))


# In[ ]:




