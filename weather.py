import requests


def capitalize_city_name(input_str):
    # Split the input string into words
    words = input_str.split()

    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words into a single string
    result_str = ' '.join(capitalized_words)

    return result_str


# Read API key from "api_key.txt" file
api_key = open('api_key.txt','r').read()

# base_url variable to store url (ver 2.5)
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# Welcome banner
print("Welcome to weather forcast")

# get the city name
city_name = input("Please enter the city name: ")

# Check the city name input
print("\nChecking the current weather of",capitalize_city_name(city_name),"\n")

# Complete API url address with variables
complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"

# Get method of request module (return response)
api_response = requests.get(complete_url)

# convert response into json format 
result_in_json = api_response.json()

# Check if the response contains valid data
if result_in_json["cod"] == 200:

    # Store the value of "main" key in variable "api_main_dt"
    api_main_dt = result_in_json["main"]
  
    # Store the value of "temp" key
    current_temperature = api_main_dt["temp"]
  
    # Store the value of "feels_like" key
    current_feels_like = api_main_dt["feels_like"]

    # Store the value of "humidity" key of y
    current_humidity = api_main_dt["humidity"]

    # Store the value of "weather" key in "api_weather_dt" variable
    api_weather_dt = result_in_json["weather"]

    # Store the value of "description" key at the 0th index of "api_weather_dt"
    weather_description = api_weather_dt[0]["description"]

    # Store the value of "sys" key in "api_sys_dt" variable
    api_sys_dt = result_in_json["sys"]

    # Store the value of "country" key in "weather_country" variable
    weather_country = api_sys_dt["country"]

    # Print the result in separate lines
    print(" Temperature (in Celsius) = " +
                    str(current_temperature) +
          "\n Feels like (in Celsius) = " +
                    str(current_feels_like) +
          "\n Humidity (in percentage) = " +
                    str(current_humidity) +
          "\n Description = " +
                    str(weather_description) +
          "\n Country = " +
                    str(weather_country))
    
elif result_in_json["cod"] == 401:
    print("Incorrect API key! Please check the API key value.")
elif result_in_json["cod"] == "404":
    print("City Not Found!")
elif result_in_json["cod"] == "400":
    print("City entry cannot accept empty value!")
else:
    print("Something went wrong!")

print("\n")