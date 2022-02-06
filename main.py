import requests, time
def main():
    x, y, t = input("Enter the coords and time: ").split()
    t = str(int(time.time() - int(t)))

    #https: // api.openweathermap.org / data / 2.5 / onecall / timemachine?lat = {lat} & lon = {lon} & dt = {time} & appid = {APIkey}

    api_key = 'b8a0167de4e3b9dd8c211ec3dd2f98f6'
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=" + x +"&lon=" + y + "&dt=" + t + "&appid=b8a0167de4e3b9dd8c211ec3dd2f98f6")
    data = response.json()
    print(data)


if __name__ == "__main__":
    main()