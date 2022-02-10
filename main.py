import requests, time, csv

import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers


def data_request_coord(x, y, t):
    # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
    # appid = {APIkey}

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + x + "&lon=" + y + "&dt=" + t + "&appid=" + API_KEY)
    data = response.json()
    print(data)
    print("Temp: " + str(round(data['current']['temp'] - 273.15, 2)) + "C")


def data_request_city(city, t):
    # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
    # appid = {APIkey}

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&dt=" + str(t) + "&appid=" + API_KEY)
    latitude = str(response.json()['coord']['lat'])
    longitude = str(response.json()['coord']['lon'])
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + latitude + "&lon=" + longitude + "&dt=" + str(
            t) + "&appid=" + API_KEY)
    # data = response.json()
    # celsius = round(data['current']['temp']-273.15, 2)
    return response.json()


def input_data():
    # x, y, t = input("Enter the coords and time: ").split()
    city, t = input("Enter the city name and time: ").split(sep=', ')
    t = str(int(time.time() - int(t)))
    # data_request_coord(x, y, t)
    return city, t


def record_data(data_list):
    with open('fiveDays.csv', 'w') as dataCollected:
        writer = csv.DictWriter(dataCollected,
                                fieldnames=['dt', 'temp', 'feels_like', 'humidity', 'pressure', 'wind_speed',
                                            'wind_deg', 'uvi', 'sunset', 'wind_gust', 'clouds', 'visibility', 'sunrise',
                                            'dew_point', 'weather', 'rain', 'snow'])
        writer.writeheader()
        writer.writerows(data_list)

def train():
    weather_train = pd.read_csv(
        "fiveDays.csv")

    #iterate through every value in weather_train and convert it to a float

    try:
        weather_train.pop('rain')
        weather_train.pop('snow')
        weather_train.pop('dew_point')
        weather_train.pop('visibility')
        weather_train.pop('feels like')
        weather_train.pop('sunrise')
        weather_train.pop('sunset')
        weather_train.pop('wind_gust')
        weather_train.pop('weather')
    except:
        pass
    print(weather_train)

    weather_train.head()
    weather_features = weather_train.copy()
    weather_labels = weather_features.pop('temp')
    #weather_labels = weather_features.pop('weather')
    """
    assert not np.any(np.isnan(weather_labels))
    normalize = layers.Normalization()
    weather_features = np.asarray(weather_features).astype(np.float32)
    weather_labels = np.asarray(weather_labels).astype(np.float32)
    normalize.adapt(weather_features)
    norm_weather_model = tf.keras.Sequential([
        normalize,
        layers.Dense(64),
        layers.Dense(2)
    ])
"""

    weather_features = np.asarray(weather_features).astype(np.float32)
    weather_labels = np.asarray(weather_labels).astype(np.float32)

    weather_model = tf.keras.Sequential([
        layers.Dense(64),
        layers.Dense(1)
    ])

    weather_model.compile(loss=tf.losses.MeanSquaredError(),
                          optimizer=tf.optimizers.Adam())

    weather_model.fit(weather_features, weather_labels, epochs=100)

    weather_model.save('test')
    reloaded = tf.keras.models.load_model('test')


    print(reloaded.predict(weather_features))


def collect_save():
    city, endTime = input_data()
    dataList = []
    for i in range(48, 0, -1):
        x = data_request_city(city, int(endTime) - i * 9000)['current']
        print(x)
        x['weather'] = x['weather'][0]['id']
        x.delete('sunrise')
        x.delete('sunset')
        x.delete('uvi')
        x.delete('visibility')
        time.sleep(1)
        dataList.append(x)
    record_data(dataList)


def main():
    with open('API_KEY.txt', 'r') as f:
        global API_KEY
        API_KEY = f.read()
    #collect_save()
    train()



if __name__ == "__main__":
    main()
