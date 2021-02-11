import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def get_data(path):
  data = pd.read_csv(path)
  return data


# get data
path = 'kc_house_data.csv'
data = get_data(path)

# add new features
data['price_m2'] = data['price'] / data['sqft_lot']


#================================================================
#Data Overview
#================================================================

f_attributes = st.sidebar.multiselect('Enter columns', data.columns)
f_zipcode = st.sidebar.multiselect(
  'Enter zipcode',
  data['zipcode'].unique() )



st.title('Data Overview')

if( f_zipcode != []) & (f_attributes != []):
  data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes] 
elif ( f_zipcode != []) & (f_attributes == []):
  data = data.loc[data['zipcode'].isin(f_zipcode), :]
elif ( f_zipcode == []) & (f_attributes != []):
  data = data.loc[:, f_attributes]
else:
  data = data.copy()

st.write(data)