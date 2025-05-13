# Step 1: Data Collection  
# Note: Make sure to download the owid-covid-data.csv from Our World in Data and save it in your working directory.  

import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
import plotly.express as px  

# Step 2: Data Loading & Exploration  
# Load the dataset  
df = pd.read_csv('owid-covid-data.csv')  

# Check columns  
print(df.columns)  

# Preview the first few rows  
print(df.head())  

# Identify missing values  
print(df.isnull().sum())  

# Key Columns: Focus on date, location, total_cases, total_deaths, new_cases, new_deaths, total_vaccinations, etc.  

# Step 3: Data Cleaning  
# Filter countries of interest  
countries_of_interest = ['Kenya', 'USA', 'India']  
df_filtered = df[df['location'].isin(countries_of_interest)]  

# Drop rows with missing dates or critical values  
df_filtered = df_filtered.dropna(subset=['date', 'total_cases', 'total_deaths'])  

# Convert the date column to datetime  
df_filtered['date'] = pd.to_datetime(df_filtered['date'])  

# Handle missing numeric values  
df_filtered['total_cases'].fillna(0, inplace=True)  
df_filtered['total_deaths'].fillna(0, inplace=True)  

# Step 4: Exploratory Data Analysis (EDA)  
# Plot total cases over time for selected countries  
plt.figure(figsize=(12, 6))  
for country in countries_of_interest:  
    country_data = df_filtered[df_filtered['location'] == country]  
    plt.plot(country_data['date'], country_data['total_cases'], label=country)  

plt.title('Total COVID-19 Cases Over Time')  
plt.xlabel('Date')  
plt.ylabel('Total Cases')  
plt.legend()  
plt.show()  

# Plot total deaths over time  
plt.figure(figsize=(12, 6))  
for country in countries_of_interest:  
    country_data = df_filtered[df_filtered['location'] == country]  
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)  

plt.title('Total COVID-19 Deaths Over Time')  
plt.xlabel('Date')  
plt.ylabel('Total Deaths')  
plt.legend()  
plt.show()  

# Calculate the death rate  
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']  

# Step 5: Visualizing Vaccination Progress  
# Plot cumulative vaccinations over time for selected countries  
plt.figure(figsize=(12, 6))  
for country in countries_of_interest:  
    country_data = df_filtered[df_filtered['location'] == country]  
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)  

plt.title('Cumulative Vaccinations Over Time')  
plt.xlabel('Date')  
plt.ylabel('Total Vaccinations')  
plt.legend()  
plt.show()  

# Step 6: Optional - Build a Choropleth Map  
# Prepare a dataframe with iso_code and total_cases for the latest date  
latest_data = df_filtered[df_filtered['date'] == df_filtered['date'].max()]  
fig = px.choropleth(latest_data,  
                    locations='iso_code',  
                    color='total_cases',  
                    hover_name='location',  
                    color_continuous_scale=px.colors.sequential.Plasma,  
                    title='COVID-19 Cases by Country')  

fig.show()  

# Step 7: Insights & Reporting  
# Document insights and findings below this point in markdown cells (in a Jupyter Notebook).