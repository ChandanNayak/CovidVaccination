# Databricks notebook source
# MAGIC %md
# MAGIC # Co-Win public APIs list 
# MAGIC https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2
# MAGIC 
# MAGIC ### Metadata APIs
# MAGIC #### Get states
# MAGIC ##### /v2/admin/location/states
# MAGIC ##### https://cdn-api.co-vin.in/api/v2/admin/location/states
# MAGIC 
# MAGIC #### Get list of districts
# MAGIC ##### /v2/admin/location/districts/{state_id}
# MAGIC ##### https://cdn-api.co-vin.in/api/v2/admin/location/districts/16 - For Karnataka
# MAGIC 
# MAGIC #### Get vaccination sessions by district for 7 days
# MAGIC ##### /v2/appointment/sessions/public/calendarByDistrict
# MAGIC ##### https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}

# COMMAND ----------

import requests
import datetime
import json
import pandas as pd

#!pip install streamlit
import streamlit as st

from copy import deepcopy

# COMMAND ----------
st.title("Covid vaccination availibility-India")

states = pd.read_csv(r"https://raw.githubusercontent.com/ChandanNayak/Covid/main/state.csv", error_bad_lines=False)
state_list= list(states["State_Name"])
stateName= st.selectbox('Select State',state_list)

districts= pd.read_csv(r"https://raw.githubusercontent.com/ChandanNayak/Covid/main/state-district.csv", error_bad_lines=False)
districtsFullList=districts.values.tolist()
district_list=[]
for elem in districtsFullList:
    if elem[1] == stateName:
        district_list.append(elem[3])
districtName= st.selectbox('Select District',district_list)

districtID=0
district_dict=dict(zip(districts["District_Name"],districts["District_ID"]))
districtID=district_dict[districtName]
# COMMAND ----------

minimumAge = int(st.slider('Select Age', 1, 100, 30))
checkDuration = int(st.slider('Select Duration', 1, 100, 30))

# COMMAND ----------

#Calculate date range and present in expected format
date_list = [datetime.datetime.today() + datetime.timedelta(days=x) for x in range(checkDuration)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

# COMMAND ----------

headerList=['Availibility Date','Center Name','Zone Name','Pin Code','Fee Type','Available Capacity','Vaccine Name']

valueList=[]
emptyList=[['na.','na.','na.','na.','na.','na.','na.']]
for date in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(districtID, date)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        if resp_json["centers"]:
            for center in resp_json["centers"]:
                for session in center["sessions"]:
                    if session["min_age_limit"] <= minimumAge and int(session["available_capacity"]) > 0:
                        valueList.append([date, center["name"], center["block_name"], center["pincode"], center["fee_type"], session["available_capacity"], session["vaccine"]])

# COMMAND ----------

if valueList==[]:
    df=pd.DataFrame(emptyList)
else:
    df=pd.DataFrame(valueList)    
df.columns=headerList

table=deepcopy(df)
st.table(table)
