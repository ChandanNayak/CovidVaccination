# Covid Vaccination Appointment
## Co-Win public APIs list 
https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2

##Metadata APIs
### Get states - /v2/admin/location/states
https://cdn-api.co-vin.in/api/v2/admin/location/states

### Get list of districts- /v2/admin/location/districts/{state_id}
https://cdn-api.co-vin.in/api/v2/admin/location/districts/16 - For Karnataka

### Get vaccination sessions by district for 7 days- /v2/appointment/sessions/public/calendarByDistrict
https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}

# To run the code on local computer 
1. Download contents into local computer 
2. Open command prompt.
3. Navigate to folder where code is stored
4. Run the command <strong>streamlit run covid_app.py</strong>

<strong>Note:</strong> Python 3 is a prerquisite and install required libraries (requests, pandas, streamlit) if not installed already. Syntax- <strong>pip install LibraryName</strong>
