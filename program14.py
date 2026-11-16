<<<<<<< HEAD
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Create a backend API
@app.route('/')
def hello():
    return "Hello World! Welcome to Python Backend Development."

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
=======
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Create a backend API
@app.route('/')
def hello():
    return "Hello World! Welcome to Python Backend Development."

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
>>>>>>> 8e757fe0d714bd26316f6391858d0a062dfbdb19
