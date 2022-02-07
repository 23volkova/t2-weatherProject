import requests, time


def dataRequestCoord(x, y, t):
    # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
    # appid = {APIkey}

    api_key = 'b8a0167de4e3b9dd8c211ec3dd2f98f6'
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + x + "&lon=" + y + "&dt=" + t + "&appid=" + api_key)
    data = response.json()
    print(data)
    print("Temp: " + str(round(data['current']['temp']-273.15, 2)) + "C")


def dataRequestCity(city, t):
    # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
    # appid = {APIkey}

    api_key = 'b8a0167de4e3b9dd8c211ec3dd2f98f6'
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&dt=" + t + "&appid=" + api_key)
    x = str(response.json()['coord']['lat'])
    y = str(response.json()['coord']['lon'])
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + x + "&lon=" + y + "&dt=" + t + "&appid=" + api_key)
    data = response.json()
    print(data)
    print("Temp: " + str(round(data['current']['temp']-273.15, 2)) + "C")


def main():
    #x, y, t = input("Enter the coords and time: ").split()
    city, t = input("Enter the city name and time: ").split()
    t = str(int(time.time() - int(t)))
    #dataRequestCoord(x, y, t)
    dataRequestCity(city, t)


if __name__ == "__main__":
    main()
