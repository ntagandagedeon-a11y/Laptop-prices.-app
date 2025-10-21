
import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the trained model
import pickle

loaded_model=pickle.load(open ('C:/Users/USER/Downloads/laptop prices/laptop_sales_data.pkl','rb'))

def laptop_price_prediction(processor_speed, RAM_size, storage_capacity):
    # Create a dataframe for the model
    new_laptop = pd.DataFrame([{
        "processor_speed": processor_speed,
        "RAM_size": RAM_size,
        "storage_capacity": storage_capacity
    }])
    
    # Predict the price
    predicted_price = loaded_model.predict(new_laptop)
    return predicted_price[0]

def main():
    st.title('NTAGANDA GEDEON SYSTEM')

    # Input fields
    processor_speed = st.text_input('Enter the processor_speed')
    Ram_size = st.text_input('Enter RAM_size')
    storage_capacity = st.text_input('Enter storage_capacity')

    if st.button('Predict Price'):
        # Convert inputs to numeric types
        try:
            processor_speed = float(processor_speed)
            RAM_size = int(RAM_size)
            storage_capacity = int(storage_capacity)
            
            # Get prediction
            price = laptop_price_prediction(processor_speed, RAM_size, storage_capacity)
            st.success(f'The predicted price for the laptop is: ${price:.2f}')
        except ValueError:
            st.error("Please enter valid numeric values for processor_speed, RAM_size, and storage_capacity.")
if __name__=='__main__':
    main()