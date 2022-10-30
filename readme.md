
# Demo of AI4Hotels project 

!['AI4Hotels'](http://ec2-52-214-49-181.eu-west-1.compute.amazonaws.com/static/images/ai4hotels_logo.svg)

This repository contains the demonstration models for the AI4Hotels project. 
To run the demonstration model, you can run the script "run_model.py" inside the scripts folder. That script forecasts electric load and occupancy based on the datasets included. The demo version hardcodes the dataset, while the final version dynamically creates the datasets used to train/run the models according to user input. 

## Quick overview

Defining the hotel characteristics (this is done by the user through the web application):
    
```python
from classes.classes import Hotel

# Defining attributes
pk = 0  # primary key (inherit from database)
hotel_name = 'Test hotel'  # hotel name
uploaded_data = '../data/demo.csv'  # data upload by client
stars = 4  # number of stars the hotel has
latitude = 28  # latitude of the hotel
longitude = -16  # longitude of the hotel
country_list = ['Spain', 'Austria', 'Germany']  # list of the countries where most of the clients come from
max_rooms = 72  # maximum number of rooms
max_capacity = 360  # maximum capacity (in number of people)
energy_forecast_horizon = 'week'  # forecast horizon (for energy can be 'day', 'week', 'month')
occupancy_forecast_horizon = 'week'  # forecast horizon (for occupancy can be 'week', 'month')
date = '2021-09-14'  # date when the forecasting is made (format "YYYY/MM/DD")

# Defining hotel
hotel = Hotel(pk, hotel_name, uploaded_data, stars, latitude, longitude, country_list, max_rooms, max_capacity)
```
    
Running the energy forecasting model and plotting the result:
```python
# Forecasting energy
energy_prediction = hotel.get_energy_forecast(energy_forecast_horizon, date)
energy_fig = hotel.plot_energy_forecast(energy_prediction, energy_forecast_horizon, date)
energy_fig.show()
```

Running the occupancy forecasting model and plotting the result:
```python 
occup_prediction = hotel.get_occupancy_forecast(occupancy_forecast_horizon, date)
occup_fig = hotel.plot_occupancy_forecast(occup_prediction, occupancy_forecast_horizon, date)
occup_fig.show()
```
    

At this moment, the demo only allows to run one model architecture (seq2seq with self-attention model). The final version will have other options.

*This project has received funding from the European Union's Horizon 2020 research and innovation programme within the framework of the I-NERGY Project funded under grant agreement No 101016508*
