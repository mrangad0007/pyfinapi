import requests

# Define the URL of the Flask endpoint
url = 'http://127.0.0.1:5000/run_script'

# Define the input data as a dictionary
data = {'company_ticker': 'AAPL'}  # Replace 'AAPL' with the actual company ticker

try:
    # Send a POST request to the Flask server with the input data
    response = requests.post(url, json=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the result returned by the Flask server
        print(response.json())
    else:
        # Print the error message if the request was not successful
        print(f'Error: {response.status_code} - {response.json()}')

except requests.RequestException as e:
    # Handle any exceptions that occur during the request
    print(f'Error: {e}')
        