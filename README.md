# URL Shortener

This is a simple URL shortener application built using Flask, a lightweight web framework in Python. The application allows users to enter a URL and generates a shorter version of it, which can be used as a redirect to the original URL.

## Features

- Accepts a long URL as input and generates a shortened version.
- Stores the mapping between the shortened URL and the original URL.
- Redirects users to the original URL when they access the shortened URL.
- Validates the input URL to ensure it is a valid URL.
- Displays success and error messages to the user.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.6 or later)
- Flask (install using `pip install flask`)
- Flask-WTF (install using `pip install flask-wtf`)

## Installation

1. Clone the repository or download the source code.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application by executing the following command in the project directory:

   ```bash
   python main.py
   ```

   This will start the Flask development server on `http://localhost:5000`.

2. Open a web browser and navigate to `http://localhost:5000`.

3. Enter a valid URL in the input field and click the "Shorten" button.

4. If the URL is valid, the application will generate a shortened URL and display it to the user as a success message.

5. Click on the shortened URL to verify that it redirects to the original URL.

## Code Structure

The project consists of the following files:

- `main.py`: Contains the Flask application code, including the routes for the index page and URL redirection. It also initializes the Flask application and sets the secret key.
- `inputform.py`: Defines the `InputForm` class, a FlaskForm subclass that represents the URL input form. It uses Flask-WTF and WTForms to define the form fields and validators.
- `templates/index.html`: The HTML template for the index page. It includes the URL input form and displays flash messages.

## Security Considerations

- The application generates the shortened URLs using `secrets.token_urlsafe()` to ensure they are difficult to guess. However, there is still a small chance of collision due to the limited length of the generated tokens.
- The `SECRET_KEY` is used to secure the session cookies and should be kept secret. It is recommended to use a strong and unique secret key in production.
- The application does not currently implement any authentication or rate limiting mechanisms. Consider adding these features if the application is exposed to untrusted users or high traffic.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---
