import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Retrieve movie information from the OMDB API
        api_key = '-----------'  # Replace with your actual OMDB API key
        title = req.params.get('title') or 'The Matrix'
        api_url = f'http://www.omdbapi.com/?apikey={api_key}&t={title}'

        # Make a GET request to the OMDB API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Check if the API response indicates an error
        if 'Error' in response.json():
            raise ValueError(response.json()['Error'])

        # Extract relevant information from the API response
        movie_data = response.json()

        # Return the movie information in the response
        return func.HttpResponse(
            body=str(movie_data),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as error:
        # Handle errors and return an appropriate response
        error_message = f"Error: {str(error)}"
        return func.HttpResponse(
            body=error_message,
            status_code=500
        )
