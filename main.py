import requests, time


def dataRequest(x, y, t):
    # https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} &
    # appid = {APIkey}

    api_key = 'b8a0167de4e3b9dd8c211ec3dd2f98f6'
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + x + "&lon=" + y + "&dt=" + t + "&appid=" + api_key)
    data = response.json()
    print(data)
    print("Temp: " + str(data['current']['temp']-273.15) + "C")


def main():
    x, y, t = input("Enter the coords and time: ").split()
    t = str(int(time.time() - int(t)))
    dataRequest(x, y, t)


if __name__ == "__main__":
    main()
