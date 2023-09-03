"""
Module Docstring: This is a brief description of what the module does.

You can provide additional details and information here, such as the purpose of the module,
how to use it, and any other relevant information.
"""

import requests

def check_rain_in_tokyo(api_key):
    """
    Checks if raining in Tokyo using openeathermap api
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    city_name = "Tokyo"
    country_code = "JP"

    # Construct the API request URL
    url = f"{base_url}?q={city_name},{country_code}&appid={api_key}"
    result = ""

    # Make the API request
    timeout_seconds = 10  # Adjust the timeout value as needed
    try:
        response = requests.get(url, timeout=timeout_seconds)
        response.raise_for_status()  # Raise an exception for HTTP errors (optional)
        # Process the response data here
        if response.status_code == 200:
            data = response.json()

            # Check for rain in the weather description
            weather_description = data["weather"][0]["description"].lower()
            if "rain" in weather_description:
                result = "It is currently raining in Tokyo."
            else:
                result = "It is not currently raining in Tokyo."
        else:
            result = "Unable to fetch weather data."

    except requests.exceptions.Timeout:
        print('The request timed out. Please check your internet connection or try again later.')

    except requests.exceptions.RequestException as err:
        print(f'An error occurred: {err}')

    return result

if __name__ == "__main__":
    API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
    print(check_rain_in_tokyo(API_KEY))
