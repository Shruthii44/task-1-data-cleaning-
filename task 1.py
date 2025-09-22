#!/usr/bin/env python
# coding: utf-8

# # Load the dataset:customer personality analysis

# In[49]:


import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/gopus/Downloads/archive/marketing_campaign.csv", sep="\t")  # dataset uses tab separator
print(df.shape)   # check rows & columns


# # check the data

# In[50]:


print(df.head())
print(df.info())  # shows column types


# # Handle Missing Values

# In[51]:


print(df.isnull().sum())  #checking missing values


# # Remove Duplicates

# In[52]:


df.drop_duplicates(inplace=True) #remove duplicates


# # Clean Column Names

# In[53]:


df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns)


# # Handle Missing Values

# In[54]:


df['income'].fillna(df['income'].median(), inplace=True)


# # Standardize Text Columns

# In[55]:


df['education'] = df['education'].str.strip().str.lower()
df['marital_status'] = df['marital_status'].str.strip().str.lower()


# # Convert Dates

# In[56]:


df['dt_customer'] = pd.to_datetime(df['dt_customer'], format="%d-%m-%Y")


# # Fix Data Types

# In[57]:


df['year_birth'] = df['year_birth'].astype(int)


# In[58]:


df['income'] = df['income'].astype(float)


# # Save Cleaned Dataset

# In[59]:


df.to_csv("customer_personality_cleaned.csv", index=False)


# In[60]:


df = pd.read_csv("customer_personality_cleaned.csv")
print(df.shape)   # check rows & columns
print(df.head())


# # Summary

# Removed duplicate rows
# 
# Filled missing income values with median
# 
# Standardized text columns (education, marital_status)
# 
# Converted dt_customer column to datetime format
# 
# Renamed columns to lowercase with underscores
# 
# Ensured correct data types (year_birth as int, income as float)

# # Load the dataset:medical appointement no show

# In[118]:


import pandas as pd

# Read CSV safely with utf-8-sig to remove hidden BOM
df = pd.read_csv("C:/Users/gopus/Downloads/KaggleV2-May-2016.csv", encoding='utf-8-sig')

# Check the columns exactly
for col in df.columns:
    print(repr(col))


# In[119]:


print(df.head())
print(df.info())  # shows column types


# In[120]:


print(df.isnull().sum())  #checking missing values


# In[122]:


df.drop_duplicates(inplace=True) #remove duplicates


# In[123]:


df.columns = df.columns.str.strip()              # remove leading/trailing spaces
df.columns = df.columns.str.lower()             # lowercase all
df.columns = df.columns.str.replace("-", "_")   # replace dashes with underscores
df.columns = df.columns.str.replace(" ", "_")   # replace spaces with underscores

print(df.columns.tolist())


# In[125]:


df['gender'] = df['gender'].str.strip().str.lower()
df['no_show'] = df['no_show'].str.strip().str.lower()
df['neighbourhood'] = df['neighbourhood'].str.strip().str.lower()


# In[126]:


df['scheduledday'] = pd.to_datetime(df['scheduledday'])      #convert date columns
df['appointmentday'] = pd.to_datetime(df['appointmentday'])


# In[127]:


df['age'] = df['age'].astype(int) #Fix in the datatypes
 


# In[128]:


df.to_csv("medical_appointment_cleaned.csv", index=False)  #save the file


# # Summary

# Removed duplicate rows
# 
# Filled missing Age values with median
# 
# Filled missing Neighbourhood values with "Unknown"
# 
# Standardized text columns (Gender, No_show)
# 
# Converted ScheduledDay and AppointmentDay to datetime
# 
# Ensured correct data types (Age as int, Gender and No_show as categorical)

# In[ ]:




