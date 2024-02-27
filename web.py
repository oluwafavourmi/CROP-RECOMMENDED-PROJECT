import streamlit as st
import joblib
import numpy as np
model = joblib.load('crop_model.pkl')


def predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    input_array = np.array((nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall))
    array_reshape = input_array.reshape(1, -1)
    prediction = model.predict(array_reshape)
    return prediction
    
st.title('Crop Recommendation App')
nitrogen = float(st.text_input('Enter the value of Nitrogen'))
phosphorus = float(st.text_input('Enter the value of Phosphorous'))
potassium = float(st.text_input('Enter the value of Potassium'))
temperature = float(st.text_input('Enter the value of Temperature'))
humidity = float(st.text_input('Enter the value of Humidity'))
ph = float(st.text_input('Enter the ph value'))
rainfall = float(st.text_input('Enter the rainfall level value')) 

if st.button('Recommend'):
    output = ''
    if predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [0]:
        output = 'Apple'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [1]:
        output = 'Banana'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [2]:
        output = 'Blackgram'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [3]:
        output = 'Chickpea'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [4]:
        output = 'Coconut'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [5]:
        output = 'Coffee'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [6]:
        output = 'Cotton'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [7]:
        output = 'Grapes'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [8]:
        output = 'Jute'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [9]:
        output = 'Kidneybeans'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [10]:
        output = 'Lentil'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [11]:
        output = 'Maize'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [12]:
        output = 'Mango'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [13]:
        output = 'Mothbeans'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [14]:
        output = 'Mungbean'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [15]:
        output = 'Muskmelon'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [16]:
        output = 'Orange'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [17]:
        output = 'Papaya'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [18]:
        output = 'Pigeonpeas'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [19]:
        output = 'Pomegranate'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [20]:
        output = 'Rice'
    elif predict_func(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall) == [21]:
        output = 'Watermelon'

    st.success('This model recommends ' + output)