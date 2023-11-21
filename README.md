# Book Recommendation system
## Prerequisites 
install a virtual environment 
 ```py -m venv .venv ```
 
## Installation
1. pip install tkinter

imports needed

1. import tkinter as Tk
2. import random
3. import CSV


## Usage
This program is a book recommendation system that recommends a book when the "Get book" button is pressed. The recommendation list was created using a CSV databased and uses the 50 most popular books according to Barnes and Noble to recommend books. 
It is a GUI and uses tkinter. 
It is a 2 page system that can be used to get another book recommendation if you do not like the recommendation or wish to get another recommendation. 
![Alt text](image.png)
![Alt text](image-1.png)



## Communcation Contract
The communcation pipe I will be using is REST/APII HTTP. 
### Data Request
1. The first step is to import flask (from flask import Flask, request, jsonify)
2. The next step is to create a Flask application ```app = Flask(__name__)``` 
3. The next step is to establish an endpoint using this method ```@app.route('/data-endpoint', methods=['GET'])```
4. The following step will be to define a method to get the data that is being requested. 
5. Within the get_data method you will need to establish the request paramenters (ex. p1 = request.args.get('p1')
6. The next step is to perform the needed operations to get the information (ex. if data: extra["data"] = data)
7. The next will be to return the data in JSON format by using jsonify (ex. jsonify(data))
8. an example call will look like this: ![Alt text](image-2.png) (I am currently using postman)

## Data Response
1. Flask automatically handles the response back to the client. So, when you ```return jsonify(data)``` the data is automatically converted to the appropriate HTTP response and sent back. 


## UML 
![Alt text](image-5.png)