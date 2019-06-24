
import pickle
import numpy as np
import pandas as pd

with open("static/adf.pkl", "rb") as f:
    adf = pickle.load(f)

with open("static/lr.pkl", "rb") as f:
    lr = pickle.load(f)

def get_random_craft(df=adf):
    """
    Input: DataFrame of aircraft in NTSB investigations.

    Output: Single, randomly selected row.
    """
    features = ['homebuilt_coded', 'light_out', 'airframe_hours', 'gross_weight',
            'visibility', 'wind_velocity', 'mid_air_acc', 'is_plane', 'instructional_flight',
            'personal_flight', 'pilot_hours', 'pro_pilot', 'pilot_age', 'cert_level',  
            'seats', 'scnd_pilot', 'since_inspection', 'airport_dist', 'y']
    craft = df.sample(1)
    return craft[features]

def to_yn(feature):
    if feature=="1":
        return "Yes"
    else:
        return "No"

def cert_decode(feature):
    if feature=="1":
        return "Basic"
    elif feature=="2":
        return "Sport"
    elif feature=="3":
        return "Class 3"
    elif feature=="4":
        return "Class 2"
    elif feature=="5":
        return "Class 1"
    else:
        return "None/unknown"

def get_display_features(craft):
    craft = craft.applymap(str)
    for var in ['is_plane', 'homebuilt_coded', 'pro_pilot', 'scnd_pilot',
               'mid_air_acc', 'instructional_flight', 'personal_flight',
               'light_out']:
        craft[var][0] = to_yn(craft[var][0])
    craft['cert_level'][0] = cert_decode(craft['cert_level'][0])
    return craft

def get_prediction(craft):
    prediction = lr.predict(craft.iloc[:, :-1])[0]
    confidence = lr.predict_proba(craft.iloc[:, :-1])[0][prediction]
    confidence = str(int(100*(round(confidence, 2))))+"%"
    return prediction, confidence
