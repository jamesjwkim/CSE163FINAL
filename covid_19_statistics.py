# -*- coding: utf-8 -*-
"""
Kim-Long Do, Jinwoo Kim, Isaac Lai
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def gdp_cases_20_richest(data):
    data = data.dropna(subset=['total_cases_per_million'])
    richest = data.groupby('location')['gdp_per_capita'].mean().nlargest(20)
    total_cases = data.groupby('location')['total_cases_per_million'].max()
    gdp_cases_rich = pd.merge(total_cases, richest, on='location')
    sns.relplot(x='gdp_per_capita', y='total_cases_per_million', 
                data=gdp_cases_rich, kind='scatter', hue='location')
    plt.title('Total COVID-19 cases per million for top 20 richest countries')
    plt.xticks(rotation=-45)
    print(gdp_cases_rich)
    
    
def gdp_cases_20_poorest(data):
    poorest = data.groupby('location')['gdp_per_capita'].mean().nsmallest(20)
    total_cases = data.groupby('location')['total_cases_per_million'].max()
    gdp_cases_poor = pd.merge(total_cases, poorest, on='location')
    sns.relplot(x='gdp_per_capita', y='total_cases_per_million', 
                data=gdp_cases_poor, kind='scatter', hue='location')
    plt.title('Total COVID-19 cases per million for top 20 poorest countries')
    plt.xticks(rotation=-45)
    print(gdp_cases_poor)
    
    
def gdp_death_20_richest(data):
    data = data.dropna(subset=['total_deaths_per_million'])
    richest = data.groupby('location')['gdp_per_capita'].mean().nlargest(20)
    total_cases = data.groupby('location')['total_deaths_per_million'].max()
    gdp_cases_rich = pd.merge(total_cases, richest, on='location')
    sns.relplot(x='gdp_per_capita', y='total_deaths_per_million', 
                data=gdp_cases_rich, kind='scatter', hue='location')
    plt.title('Total COVID-19 deaths per million for top 20 richest countries')
    plt.xticks(rotation=-45)
    print(gdp_cases_rich)    
    
    
def gdp_death_20_poorest(data):
    data = data.dropna(subset=['total_deaths_per_million'])
    poorest = data.groupby('location')['gdp_per_capita'].mean().nsmallest(20)
    total_cases = data.groupby('location')['total_deaths_per_million'].max()
    gdp_cases_poor = pd.merge(total_cases, poorest, on='location')
    sns.relplot(x='gdp_per_capita', y='total_cases_per_million', 
                data=gdp_cases_poor, kind='scatter', hue='location')
    plt.title('Total COVID-19 deaths per million for top 20 poorest countries')
    plt.xticks(rotation=-45)
    print(gdp_cases_poor)
    
    
def vaccine_positive_high(data):
    data_vacc = data.dropna(subset=['positive_rate'])
    posi_high = data_vacc.groupby('location')['positive_rate'
                                            ].mean().nlargest(20)
    vacc_count = data.groupby('location')['people_vaccinated_per_hundred'
                                          ].max()
    posi_vacc_high = pd.merge(posi_high, vacc_count, on='location')
    sns.relplot(x='positive_rate', y='people_vaccinated_per_hundred', 
                data=posi_vacc_high, kind='scatter', hue='location')
    plt.title('Relationship between 20 lowest average positive rates ' +
              'for COVID-19 and people vaccinated per hundred')
    plt.xticks(rotation=-45)    
    print(posi_vacc_high)


def vaccine_positive_low(data):
    data_vacc = data.dropna(subset=['positive_rate'])
    posi_low = data_vacc.groupby('location')['positive_rate'
                                            ].mean().nsmallest(20)
    vacc_count = data.groupby('location')['people_vaccinated_per_hundred'
                                          ].max()
    posi_vacc_low = pd.merge(posi_low, vacc_count, on='location')
    sns.relplot(x='positive_rate', y='people_vaccinated_per_hundred', 
                data=posi_vacc_low, kind='scatter', hue='location')
    plt.title('Relationship between 20 lowest average positive rates ' + 
              'for COVID-19 and people vaccinated per hundred')
    plt.xticks(rotation=-45)
    print(posi_vacc_low)
    
    
def main():
    data = pd.read_csv(
        r'data/owid-covid-data.csv')
    gdp_cases_20_richest(data)
    gdp_cases_20_poorest(data)
    gdp_death_20_richest(data)
    vaccine_positive_high(data)
    vaccine_positive_low(data)
    
    
if __name__ == '__main__':
    main()    
