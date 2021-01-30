# Flask app for plague detection using openCV
You can run this application installing Flask in your computer (```pip install flask```) and then setting up some environment variables (This is the way of windows, if you're in Linux or Mac you need to use the right syntaxis):  
1. ```$env:FLASK_APP="./src/main.py"``` this is to locate the main program
2. ```$env:FLASK_ENV="development"``` this is to set up a development server  

# Requirements

Due to the specific versions used in this project, you should create a virtual environment using ```py -3 -m venv venv```. You can't install the latest version of some packages because of the compatibility with Flutter packages, the main example is the socket one, where you need an specific version because there is no official build for Flutter so you deppend on third parties.

You can activate the virtual environment using ```.\venv\Scripts\activate```

## eventlet
You can install it using  ```pip install eventlet```. It's necessary in order to be able to broadcast to other devices using websockets.

## Flask socket.io
You need to use the 5.x.x version (```pip install flask-socketio==5```)

# Execution  
You can't run the app using ```flask run``` due to socket.io conflicts, you should use ```python .\src\main.py``` instead.