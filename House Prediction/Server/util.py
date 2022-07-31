import numpy as np
import json
import pickle

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def load_saved_artificats():
    print("loading saved artifacts.....start")
    global __data_columns
    global __locations
    with open("./artifact/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")