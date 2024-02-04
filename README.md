# Serverlessapi

# Azure Functions Movie Info API

This Azure Functions project utilizes serverless functions to retrieve movie information from the OMDB API. It provides a simple HTTP-triggered function that takes a movie title as a parameter and returns details about the movie.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Folder Structure](#folder-structure)
- [Monitoring](#monitoring)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This project demonstrates how to create an Azure Functions API with serverless functions written in Python. The HTTP-triggered function interacts with the OMDB API to fetch movie details based on the provided title.

## Getting Started

### Prerequisites
- Install python version supported for your IDE locally .
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- [Visual Studio Code](https://code.visualstudio.com/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Change into the project directory:

   ```bash
   cd your-repo
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Azure Functions project locally:

   ```bash
   func start
   ```

2. Test the function locally using a tool like cURL or a web browser:

   ```
   http://localhost:7071/api/GetMovieInfo?title=Inception
   ```

## Functionality

- Accepts a movie title as a parameter.
- Makes a request to the OMDB API to fetch movie information.
- Returns the movie details in the HTTP response.

## Folder Structure

```
- YourFunctionApp
  - GetMovieInfo
    - __init__.py
    - function.json
  - requirements.txt
  - host.json
  - local.settings.json
  - ...
```

## Monitoring

Enable and configure Application Insights for monitoring your Azure Functions. Refer to [Step 9](#9-monitor-and-diagnose) in the README for details.

## Contributing

Contributions are welcome! Please follow the guidelines outlined in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, contact [Your Name](mailto:your.email@example.com).

```

Replace `your-username` and `your-repo` with your actual GitHub username and repository name. Adjust the contact information, license, and other sections as needed for your project. This README provides an overview, instructions for getting started, details about functionality, and information on how to contribute.
