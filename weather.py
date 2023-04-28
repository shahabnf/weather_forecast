import requests


# Default values
# city name
city_name = ""

# city name
api_key = "ABCD"


# base_url variable to store url
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# Welcome banner
print("Welcome to weather forcast")

# get the city name
city_name = input("Please enter the city name: ")

# Check the city name input
print(city_name)

# Add API key
api_key = input("Please enter the API key: ")

# Check the API input
print(api_key)

# Complete API url address with variables
complete_url = base_url + "q=" + city_name + "&appid=" + api_key

# Get method of request module (return response)
api_response = requests.get(complete_url)

# Check the response value
print(api_response)

# convert response into json format 
result_in_json = api_response.json()

# Check the json response value
print(result_in_json)
