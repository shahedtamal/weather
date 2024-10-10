import requests

def get_weather(city, 8b0aecfc74ac83173bceae245b51b786):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={8b0aecfc74ac83173bceae245b51b786}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
    else:
        print("City not found!")

def main():
    api_key = '8b0aecfc74ac83173bceae245b51b786'  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
