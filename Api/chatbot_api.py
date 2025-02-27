import requests
import json

# Function to get chatbot response via API
def get_chatbot_response(url, question, headers):
    
    params = {'q': question}

    try:
        # Send the GET request with the Bearer token in headers
        response = requests.get(url, params=params, headers=headers)

        # Check if the request was successful
        response.raise_for_status()  # Raises an error for HTTP errors

        # Attempt to parse the response as JSON
        try:
            response_json = response.json()  # Assuming the response is in JSON format
            return response_json
        except ValueError as json_err:
            print(f"JSON decode error: {json_err}")
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None