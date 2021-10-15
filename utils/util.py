import json
import pickle
import numpy as np
import model
import sklearn

__location=None
__data_columns=None
__model=None
def get_estimated_price(location,sqft,bhk,bath):
    try :
        col_index=__data_columns.index(location.lower())
        x=np.zeros(len(__data_columns))
        x[0]=sqft
        x[1]=bath
        x[2]=bhk
        if col_index > 0:
            x[col_index]=1
        return round(__model.predict([x])[0],2)
    except ValueError:
        error=f"{location.lower()} is not present in location list"
        return error


def load_saved_modeldetails():
    print("Loading saved model details start.....!")
    global __data_columns
    global __location
    with open("model/location_name.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __location=__data_columns[3:]

    global __model
    with open("model/Bangalore_House_Price_model.pickle",'rb') as f:
        __model = pickle.load(f)

    print("Loading saved model details completed.....!")
def get_data_columns():
    return __data_columns

def get_location_name():
    return __location

if __name__ == '__main__':
    load_saved_modeldetails()
    get_location_name()
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
