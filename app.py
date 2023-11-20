from flask import Flask, render_template
from routes import configure_routes

# Initialize the Flask application
app = Flask(__name__)

# Configure the routes from the routes.py file
configure_routes(app)


# Run the application
if __name__ == '__main__':
    # Enabling debug mode for development purposes
    app.run(debug=True, host='127.0.0.1', port = 8423)
