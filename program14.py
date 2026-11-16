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
