#Choose an API from RapidAPI that interests you—make sure it has a free tier and simple authentication. 
# Write a Python script that makes a request to your selected API, using the appropriate endpoint and parameters to retrieve data. 
# Save the response data to a variable, and handle it as JSON to work with nested structures. 
# Extract a specific item from the nested dictionary in the response, and 
# print a statement that meaningfully displays this information. 


import requests

# Endpoint that data would be retrieved from
url = "https://weather-api-by-any-city.p.rapidapi.com/weather/Tennessee"


# Security: API keys and host
headers = {
	"x-rapidapi-key": "253d1bf891mshcbd5624ec8e8861p1e2923jsn9a66729f68d9",
	"x-rapidapi-host": "weather-api-by-any-city.p.rapidapi.com"
}


# Create variable to refrerence the parameters of the .get() above
response = requests.get(url, headers=headers)


# Collect JSON response into a variable for easier parsing
print(response.json())

