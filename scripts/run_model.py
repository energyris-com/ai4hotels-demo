from classes.classes import Hotel


if __name__ == '__main__':
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

    # Forecasting energy
    energy_prediction = hotel.get_energy_forecast(energy_forecast_horizon, date)
    energy_fig = hotel.plot_energy_forecast(energy_prediction, energy_forecast_horizon, date)
    energy_fig.show()

    # Forecasting occupancy
    occup_prediction = hotel.get_occupancy_forecast(occupancy_forecast_horizon, date)
    occup_fig = hotel.plot_occupancy_forecast(occup_prediction, occupancy_forecast_horizon, date)
    occup_fig.show()
