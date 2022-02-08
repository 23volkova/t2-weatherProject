import requests, time, csv


def data_request_coord(x, y, t):
    # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
    # appid = {APIkey}

    api_key = 'b8a0167de4e3b9dd8c211ec3dd2f98f6'
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + x + "&lon=" + y + "&dt=" + t + "&appid=" + api_key)
    data = response.json()
    print(data)
    print("Temp: " + str(round(data['current']['temp'] - 273.15, 2)) + "C")


def data_request_city(city, t):
    # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
    # appid = {APIkey}

    api_key = 'b8a0167de4e3b9dd8c211ec3dd2f98f6'
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&dt=" + str(t) + "&appid=" + api_key)
    latitude = str(response.json()['coord']['lat'])
    longitude = str(response.json()['coord']['lon'])
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + latitude + "&lon=" + longitude + "&dt=" + str(t) + "&appid=" + api_key)
    # data = response.json()
    # celcius = round(data['current']['temp']-273.15, 2)
    return response.json()


def input_data():
    # x, y, t = input("Enter the coords and time: ").split()
    city, t = input("Enter the city name and time: ").split()
    t = str(int(time.time() - int(t)))
    # data_request_coord(x, y, t)
    return city, t


def record_data(dataList):
    with open('fiveDays.csv', 'w') as dataCollected:
        writer = csv.DictWriter(dataCollected, fieldnames=['dt', 'temp', 'feels_like', 'humidity', 'pressure', 'wind_speed', 'wind_deg', 'weather', 'uvi', 'sunset', 'wind_gust', 'clouds', 'visibility', 'sunrise', 'dew_point'])
        writer.writeheader()
        writer.writerows(dataList)


def main():
    city, endTime = input_data()
    dataList = []
    for i in range(48, 0, -1):
        x = data_request_city(city, int(endTime) - i * 9000)['current']
        time.sleep(1)
        dataList.append(x)
    record_data(dataList)


if __name__ == "__main__":
    main()
