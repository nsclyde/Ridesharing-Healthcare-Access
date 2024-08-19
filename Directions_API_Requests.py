# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import os
import urllib.request
import json
from tqdm import tqdm


#First get Medicare Part D data from each year

os.chdir("C:/Users/nsclyde/OneDrive - Washington University in St. Louis/TA Responsibilities/Research/Uber Project/Reproduction Folder/")


# Load the datasets
providers_2013 = pd.read_csv("Data/Medicare_Part_D_Prescribers_by_Provider_Dataset_2013.csv")
providers_2014 = pd.read_csv("Data/Medicare_Part_D_Prescribers_by_Provider_Dataset_2014.csv")
providers_2015 = pd.read_csv("Data/Medicare_Part_D_Prescribers_by_Provider_Dataset_2015.csv")
providers_2016 = pd.read_csv("Data/Medicare_Part_D_Prescriber_by_Provider_Dataset_2016.csv")
providers_2017 = pd.read_csv("Data/Medicare_Part_D_Prescribers_by_Provider_2017_version2.csv")
providers_2018 = pd.read_csv("Data/Medicare_Part_D_Prescribers_by_Provider_2018.csv")
providers_2019 = pd.read_csv("Data/Medicare_Part_D_Prescribers_by_Provider_2019.csv")
providers_2020 = pd.read_csv("Data/Medicare_Part_D_Prescribers_by_Provider_2020.csv")

# Correct column name discrepancies for the 2017 dataset
providers_2017.rename(columns={
    'Prscrbr_NPI': 'PRSCRBR_NPI',
    'Prscrbr_Zip5': 'Prscrbr_zip5',
    'Prscrbr_Type_Src': 'Prscrbr_Type_src'
}, inplace=True)

# Defining yearindicator for each dataset
providers_2013['yearindicator'] = 2013
providers_2014['yearindicator'] = 2014
providers_2015['yearindicator'] = 2015
providers_2016['yearindicator'] = 2016
providers_2017['yearindicator'] = 2017
providers_2018['yearindicator'] = 2018
providers_2019['yearindicator'] = 2019
providers_2020['yearindicator'] = 2020

# Combine all datasets
providers = pd.concat([providers_2013, providers_2014, providers_2015, providers_2016, providers_2017, providers_2018, providers_2019, providers_2020], ignore_index=True)

# Create uber_providers DataFrame
uber_providers = providers.copy()
uber_providers['Prscrbr_zip5'] = uber_providers['Prscrbr_zip5'].astype(str)

# Create fulladdress column
uber_providers['fulladdress'] = uber_providers['Prscrbr_St1'] + " " + uber_providers['Prscrbr_City'] + " " + uber_providers['Prscrbr_State_Abrvtn'] + " " + uber_providers['Prscrbr_zip5']

# Fix a specific address
uber_providers['fulladdress'] = uber_providers['fulladdress'].replace("Department Of Family & Community Medicine Lubbock TX 79430", '3601 4th St STOP 8195 Lubbock TX 79430')

#create dfs of unique addresses in each city
Austin_Addresses = pd.DataFrame(uber_providers[uber_providers['Prscrbr_City'] == "Austin"]['fulladdress'].unique(), columns=['Address'])
Amarillo_Addresses = pd.DataFrame(uber_providers[uber_providers['Prscrbr_City'] == "Amarillo"]['fulladdress'].unique(), columns=['Address'])
ElPaso_Addresses = pd.DataFrame(uber_providers[uber_providers['Prscrbr_City'] == "El Paso"]['fulladdress'].unique(), columns=['Address'])
Lubbock_Addresses = pd.DataFrame(uber_providers[uber_providers['Prscrbr_City'] == "Lubbock"]['fulladdress'].unique(), columns=['Address'])

#Zipcode populations data pulled from S0101 Ammerican Community Survey table from Census Data for the year 2016. 
#Percentage indicates the percentage of 65+ old individuals in a given zipcode divided by total 65+ old invididuals in the city. 
zipcode_populations = pd.read_csv("Data/zipcode_populations.csv")





#### Austin


Austin_Addresses["distance_1_json"]=np.nan
Austin_Addresses["distance_2_json"]=np.nan
Austin_Addresses["distance_3_json"]=np.nan
Austin_Addresses["distance_4_json"]=np.nan
Austin_Addresses["distance_5_json"]=np.nan
Austin_Addresses["distance_6_json"]=np.nan
Austin_Addresses["distance_7_json"]=np.nan
Austin_Addresses["distance_8_json"]=np.nan
Austin_Addresses["distance_9_json"]=np.nan
Austin_Addresses["distance_10_json"]=np.nan

names_json_columns=["distance_1_json","distance_2_json","distance_3_json","distance_4_json","distance_5_json","distance_6_json","distance_7_json","distance_8_json","distance_9_json","distance_10_json"]


# use zipcode data to randomly select 10 based off population of older individuals
city_zipcodes=zipcode_populations[zipcode_populations['City']=="Austin"]
percentage_list= city_zipcodes.percentage.values.tolist()
zips_list= city_zipcodes.Zip.values.tolist()

zips_random=[]
j=1
while j<11:
    zips_random.append(np.random.choice(zips_list, p=percentage_list))
    j+=1

#These are the 10 random Austin zipcodes (with replacement)
zips_random=['78734',
 '78744',
 '78744',
 '78704',
 '78681',
 '78759',
 '78744',
 '78723',
 '78750',
 '78758']


endpoint="https://maps.googleapis.com/maps/api/directions/json?"
api_key="INSERT YOUR API KEY HERE" #Need to put your API key here
mode="transit"
departure_time="1681309809" #this will likely need to be changed for replication since Google only allows time periods close to the current one


for dest_rows in tqdm(range(len(Austin_Addresses.loc[0:,]))):
    destination=Austin_Addresses.iloc[dest_rows+0]["Address"].replace(" ","+").replace("#","")
    for origin_rows in range(10):
        origin=("Texas "+zips_random[origin_rows]).replace(" ","+")
        nav_request= "origin={}&destination={}&mode={}&departure_time={}&key={}".format(origin, destination, mode, departure_time, api_key)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        Austin_Addresses.loc[dest_rows+0, names_json_columns[origin_rows]]=str(json.loads(response))


#### El Paso

ElPaso_Addresses["distance_1_json"]=np.nan
ElPaso_Addresses["distance_2_json"]=np.nan
ElPaso_Addresses["distance_3_json"]=np.nan
ElPaso_Addresses["distance_4_json"]=np.nan
ElPaso_Addresses["distance_5_json"]=np.nan
ElPaso_Addresses["distance_6_json"]=np.nan
ElPaso_Addresses["distance_7_json"]=np.nan
ElPaso_Addresses["distance_8_json"]=np.nan
ElPaso_Addresses["distance_9_json"]=np.nan
ElPaso_Addresses["distance_10_json"]=np.nan

city_zipcodes=zipcode_populations[zipcode_populations['City']=="El Paso"]
percentage_list= city_zipcodes.percentage.values.tolist()
zips_list= city_zipcodes.Zip.values.tolist()

zips_random=[]
j=1
while j<11:
    zips_random.append(np.random.choice(zips_list, p=percentage_list))
    j+=1

#These are the 10 random El Paso zipcodes (with replacement)

zips_random=['79936',
 '79936',
 '79938',
 '79904',
 '79902',
 '79927',
 '79924',
 '79907',
 '79905',
 '79905']


for dest_rows in tqdm(range(len(ElPaso_Addresses))):
    destination=ElPaso_Addresses.iloc[dest_rows]["Address"].replace(" ","+").replace("#","")
    for origin_rows in range(10):
        origin=("Texas "+zips_random[origin_rows]).replace(" ","+")
        nav_request= "origin={}&destination={}&mode={}&departure_time={}&key={}".format(origin, destination, mode, departure_time, api_key)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        ElPaso_Addresses.loc[dest_rows, names_json_columns[origin_rows]]=str(json.loads(response))


#### Lubbock

Lubbock_Addresses["distance_1_json"]=np.nan
Lubbock_Addresses["distance_2_json"]=np.nan
Lubbock_Addresses["distance_3_json"]=np.nan
Lubbock_Addresses["distance_4_json"]=np.nan
Lubbock_Addresses["distance_5_json"]=np.nan
Lubbock_Addresses["distance_6_json"]=np.nan
Lubbock_Addresses["distance_7_json"]=np.nan
Lubbock_Addresses["distance_8_json"]=np.nan
Lubbock_Addresses["distance_9_json"]=np.nan
Lubbock_Addresses["distance_10_json"]=np.nan

city_zipcodes=zipcode_populations[zipcode_populations['City']=="Lubbock"]
percentage_list= city_zipcodes.percentage.values.tolist()
zips_list= city_zipcodes.Zip.values.tolist()

zips_random=[]
j=1
while j<11:
    zips_random.append(np.random.choice(zips_list, p=percentage_list))
    j+=1

#These are the 10 random El Paso zipcodes (with replacement)

zips_random=['79416',
 '79404',
 '79424',
 '79413',
 '79424',
 '79412',
 '79424',
 '79424',
 '79404',
 '79424']


endpoint="https://maps.googleapis.com/maps/api/directions/json?"
api_key="INSERT YOUR API KEY HERE" #Need to put your API key here
mode="transit"
departure_time="1698787809"  #this will likely need to be changed for replication since Google only allows time periods close to the current one

for dest_rows in tqdm(range(len(Lubbock_Addresses.loc[0:,]))):
    destination=Lubbock_Addresses.iloc[dest_rows+0]["Address"].replace(" ","+").replace("#","")
    for origin_rows in [0,1,2,3,4,5,6,7,8,9]:
        origin=("Texas "+zips_random[origin_rows]).replace(" ","+")
        nav_request= "origin={}&destination={}&mode={}&departure_time={}&key={}".format(origin, destination, mode, departure_time, api_key)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        Lubbock_Addresses.loc[dest_rows+0, names_json_columns[origin_rows]]=str(json.loads(response))

#### Amarillo


Amarillo_Addresses["distance_1_json"]=np.nan
Amarillo_Addresses["distance_2_json"]=np.nan
Amarillo_Addresses["distance_3_json"]=np.nan
Amarillo_Addresses["distance_4_json"]=np.nan
Amarillo_Addresses["distance_5_json"]=np.nan
Amarillo_Addresses["distance_6_json"]=np.nan
Amarillo_Addresses["distance_7_json"]=np.nan
Amarillo_Addresses["distance_8_json"]=np.nan
Amarillo_Addresses["distance_9_json"]=np.nan
Amarillo_Addresses["distance_10_json"]=np.nan

names_json_columns=["distance_1_json","distance_2_json","distance_3_json","distance_4_json","distance_5_json","distance_6_json","distance_7_json","distance_8_json","distance_9_json","distance_10_json"]

city_zipcodes=zipcode_populations[zipcode_populations['City']=="Amarillo"]
percentage_list= city_zipcodes.percentage.values.tolist()
zips_list= city_zipcodes.Zip.values.tolist()

zips_random=[]
j=1
while j<11:
    zips_random.append(np.random.choice(zips_list, p=percentage_list))
    j+=1

#These are the 10 random Amarillo zipcodes (with replacement)

zips_random=['79108',
 '79110',
 '79110',
 '79110',
 '79109',
 '79106',
 '79109',
 '79101',
 '79104',
 '79106']

#ElPaso_Addresses["Address"][533]='7610 State Highway 71 Austin TX 78735'

endpoint="https://maps.googleapis.com/maps/api/directions/json?"
api_key="INSERT YOUR API KEY HERE" #Need to put your API key here
mode="transit"
departure_time="1698787809"  #this will likely need to be changed for replication since Google only allows time periods close to the current one

for dest_rows in tqdm(range(len(Amarillo_Addresses))):
    destination=Amarillo_Addresses.iloc[dest_rows]["Address"].replace(" ","+").replace("#","")
    for origin_rows in [0,1,2,3,4,5,6,7,8,9]:
        origin=("Texas "+zips_random[origin_rows]).replace(" ","+")
        nav_request= "origin={}&destination={}&mode={}&departure_time={}&key={}".format(origin, destination, mode, departure_time, api_key)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        Amarillo_Addresses.loc[dest_rows, names_json_columns[origin_rows]]=str(json.loads(response))


#Now start to calculate mean_duration=mean walking duration for each of the 10 sets of directions

list_columns=['Address','distance_1_json','distance_2_json','distance_3_json','distance_4_json','distance_5_json','distance_6_json','distance_7_json','distance_8_json','distance_9_json','distance_10_json']

# initializing columns

Austin_Addresses["duration_1"]=Austin_Addresses["distance_1_json"]
Austin_Addresses["duration_2"]=Austin_Addresses["distance_2_json"]
Austin_Addresses["duration_3"]=Austin_Addresses["distance_3_json"]
Austin_Addresses["duration_4"]=Austin_Addresses["distance_4_json"]
Austin_Addresses["duration_5"]=Austin_Addresses["distance_5_json"]
Austin_Addresses["duration_6"]=Austin_Addresses["distance_6_json"]
Austin_Addresses["duration_7"]=Austin_Addresses["distance_7_json"]
Austin_Addresses["duration_8"]=Austin_Addresses["distance_8_json"]
Austin_Addresses["duration_9"]=Austin_Addresses["distance_9_json"]
Austin_Addresses["duration_10"]=Austin_Addresses["distance_10_json"]

ElPaso_Addresses["duration_1"]=ElPaso_Addresses["distance_1_json"]
ElPaso_Addresses["duration_2"]=ElPaso_Addresses["distance_2_json"]
ElPaso_Addresses["duration_3"]=ElPaso_Addresses["distance_3_json"]
ElPaso_Addresses["duration_4"]=ElPaso_Addresses["distance_4_json"]
ElPaso_Addresses["duration_5"]=ElPaso_Addresses["distance_5_json"]
ElPaso_Addresses["duration_6"]=ElPaso_Addresses["distance_6_json"]
ElPaso_Addresses["duration_7"]=ElPaso_Addresses["distance_7_json"]
ElPaso_Addresses["duration_8"]=ElPaso_Addresses["distance_8_json"]
ElPaso_Addresses["duration_9"]=ElPaso_Addresses["distance_9_json"]
ElPaso_Addresses["duration_10"]=ElPaso_Addresses["distance_10_json"]

Lubbock_Addresses["duration_1"]=Lubbock_Addresses["distance_1_json"]
Lubbock_Addresses["duration_2"]=Lubbock_Addresses["distance_2_json"]
Lubbock_Addresses["duration_3"]=Lubbock_Addresses["distance_3_json"]
Lubbock_Addresses["duration_4"]=Lubbock_Addresses["distance_4_json"]
Lubbock_Addresses["duration_5"]=Lubbock_Addresses["distance_5_json"]
Lubbock_Addresses["duration_6"]=Lubbock_Addresses["distance_6_json"]
Lubbock_Addresses["duration_7"]=Lubbock_Addresses["distance_7_json"]
Lubbock_Addresses["duration_8"]=Lubbock_Addresses["distance_8_json"]
Lubbock_Addresses["duration_9"]=Lubbock_Addresses["distance_9_json"]
Lubbock_Addresses["duration_10"]=Lubbock_Addresses["distance_10_json"]

Amarillo_Addresses["duration_1"]=Amarillo_Addresses["distance_1_json"]
Amarillo_Addresses["duration_2"]=Amarillo_Addresses["distance_2_json"]
Amarillo_Addresses["duration_3"]=Amarillo_Addresses["distance_3_json"]
Amarillo_Addresses["duration_4"]=Amarillo_Addresses["distance_4_json"]
Amarillo_Addresses["duration_5"]=Amarillo_Addresses["distance_5_json"]
Amarillo_Addresses["duration_6"]=Amarillo_Addresses["distance_6_json"]
Amarillo_Addresses["duration_7"]=Amarillo_Addresses["distance_7_json"]
Amarillo_Addresses["duration_8"]=Amarillo_Addresses["distance_8_json"]
Amarillo_Addresses["duration_9"]=Amarillo_Addresses["distance_9_json"]
Amarillo_Addresses["duration_10"]=Amarillo_Addresses["distance_10_json"]


#define function that returns duration or -1 if it cannot find transit directions
def get_walking_duration(data):
    if data[2:11]=='available':
        return -1
    elif eval(data)['status']=='NOT_FOUND':
        return -1
    else:
        data=eval(data)
        total_walking_duration = 0
    
        for leg in data['routes'][0]['legs']:
            for step in leg['steps']:
                if step['travel_mode'] == 'WALKING':
                    total_walking_duration += step['duration']['value']
    
        return total_walking_duration
    
list_columns=['duration_1','duration_2','duration_3','duration_4','duration_5','duration_6','duration_7','duration_8','duration_9','duration_10']


for column in tqdm(list_columns):
    Austin_Addresses[column] = Austin_Addresses[column].apply(get_walking_duration)
    ElPaso_Addresses[column] = ElPaso_Addresses[column].apply(get_walking_duration)
    Lubbock_Addresses[column] = Lubbock_Addresses[column].apply(get_walking_duration)
    Amarillo_Addresses[column] = Amarillo_Addresses[column].apply(get_walking_duration)
 


max_duration = Austin_Addresses[['duration_1','duration_2','duration_3','duration_4','duration_5','duration_6','duration_7','duration_8','duration_9','duration_10']].max().max()
max_duration=max(max_duration,ElPaso_Addresses[['duration_1','duration_2','duration_3','duration_4','duration_5','duration_6','duration_7','duration_8','duration_9','duration_10']].max().max())
max_duration=max(max_duration,Lubbock_Addresses[['duration_1','duration_2','duration_3','duration_4','duration_5','duration_6','duration_7','duration_8','duration_9','duration_10']].max().max())
max_duration=max(max_duration,Amarillo_Addresses[['duration_1','duration_2','duration_3','duration_4','duration_5','duration_6','duration_7','duration_8','duration_9','duration_10']].max().max())

#max walking duration was 6999 for our requests
max_duration=6999

# replace any values from places that couldn't find transit results with the max duration
for columns in list_columns:
    Austin_Addresses.loc[Austin_Addresses[columns]==-1,columns]=max_duration
    ElPaso_Addresses.loc[ElPaso_Addresses[columns]==-1,columns]=max_duration
    Lubbock_Addresses.loc[Lubbock_Addresses[columns]==-1,columns]=max_duration
    Amarillo_Addresses.loc[Amarillo_Addresses[columns]==-1,columns]=max_duration
 
# calculate mean duration for each set of addresses

Austin_Addresses["mean_duration"]=(Austin_Addresses["duration_1"]+\
    Austin_Addresses["duration_2"]+Austin_Addresses["duration_3"]+\
        Austin_Addresses["duration_4"]+Austin_Addresses["duration_5"]+\
        Austin_Addresses["duration_6"]+Austin_Addresses["duration_7"]\
            +Austin_Addresses["duration_8"]+Austin_Addresses["duration_9"]
            +Austin_Addresses["duration_10"])/10

ElPaso_Addresses["mean_duration"]=(ElPaso_Addresses["duration_1"]+\
    ElPaso_Addresses["duration_2"]+ElPaso_Addresses["duration_3"]+\
        ElPaso_Addresses["duration_4"]+ElPaso_Addresses["duration_5"]+\
        ElPaso_Addresses["duration_6"]+ElPaso_Addresses["duration_7"]\
            +ElPaso_Addresses["duration_8"]+ElPaso_Addresses["duration_9"]
            +ElPaso_Addresses["duration_10"])/10



Lubbock_Addresses["mean_duration"]=(Lubbock_Addresses["duration_1"]+\
    Lubbock_Addresses["duration_2"]+Lubbock_Addresses["duration_3"]+\
        Lubbock_Addresses["duration_4"]+Lubbock_Addresses["duration_5"]+\
        Lubbock_Addresses["duration_6"]+Lubbock_Addresses["duration_7"]\
            +Lubbock_Addresses["duration_8"]+Lubbock_Addresses["duration_9"]
            +Lubbock_Addresses["duration_10"])/10


Amarillo_Addresses["mean_duration"]=(Amarillo_Addresses["duration_1"]+\
    Amarillo_Addresses["duration_2"]+Amarillo_Addresses["duration_3"]+\
        Amarillo_Addresses["duration_4"]+Amarillo_Addresses["duration_5"]+\
        Amarillo_Addresses["duration_6"]+Amarillo_Addresses["duration_7"]\
            +Amarillo_Addresses["duration_8"]+Amarillo_Addresses["duration_9"]
            +Amarillo_Addresses["duration_10"])/10
    
Addresses = pd.concat([Austin_Addresses, Amarillo_Addresses, ElPaso_Addresses, Lubbock_Addresses], ignore_index=True)

Addresses = Addresses[["Address", "mean_duration"]]

# add this mean_duration data back to the main file

uber_providers = pd.merge(uber_providers, Addresses, how="outer", left_on="fulladdress", right_on="Address")

uber_providers.to_csv("Data/uber_providers_Reproduction.csv")
