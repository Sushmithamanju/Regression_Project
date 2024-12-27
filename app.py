import streamlit as st
import pandas as pd
import numpy as np
import json
import requests

st.title('Real Estate Price Prediction')


with open('input_options.json') as f:
    side_bar_options = json.load(f)
    options = {}
    for key, value in side_bar_options.items():
        if key in ['City','StateZip']:
            options[key] = st.sidebar.selectbox(key, value)
        else:
            min_val, max_val = value
            min_val=float(min_val)
            max_val=float(max_val)
            current_value = (min_val + max_val)/2
            options[key] = st.sidebar.slider(key, min_val, max_val, value=current_value)

st.write(options)

if st.button('Predict'): 
    print('IN button')
    payload = json.dumps({'inputs': options})
    response = requests.post(
        url=f"http://localhost:5000/invocations",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    prediction=response.json().get('predictions')[0]
    st.write(f"The predicted property value is:,{prediction:,}")