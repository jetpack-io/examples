from flask import Flask

# Import our routes and application code
import hello

# Declare a variable "app" with the Flask app
app = Flask(__name__)

# This is only for debugging locally. Jetpack will automatically import and run the Flask app variable declared in the line above
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
