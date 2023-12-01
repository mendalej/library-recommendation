import csv
from flask import Flask, request, jsonify

app = Flask(__name__)


history = []

def recs_history():
    with open('recommendations.csv', 'r') as file:
        readers = csv.reader(file)
        return [item for item in readers]
    
@app.route("/get_history", methods=["GET"])
def get_history():
    data = recs_history()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
