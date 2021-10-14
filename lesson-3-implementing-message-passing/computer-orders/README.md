# Computer Orders Api

This is the api created as part of the course 2. 

## IMPORTANT

DO NOT USE VS CODE TERMINAL TO TROUBLESHOT ISSUES STARTING THE APPLICATION WITH FLASK!!!

FOR SOME REASON VS CODE TERMINAL DOES NOT SHOW FULL ERROR MESSAGES!!!

## Dev Environment Setup

```
# Create virtual environment 
python3 -m venv .venv

# Activate virtual environment (always run this when openning a new terminal)
cd .venv
source bin/activate

# Install required packages
pip install -r requirements.txt

# Start the application
python app.py

# Go to http://127.0.0.1:3111/

# Using flask command line to start the application
# This can be used to automatically apply source code changes but runs on port 5000 instead of 3111
FLASK_APP=app FLASK_ENV=development flask run

# Go to http://127.0.0.1:5000/
```

