from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-data/<data_id>")
def get_data(data_id):
    user_data = {
        "data_id": data_id,
        "data_title" : "Data Title"
    }

    other = request.args.get("other")
    if other:
        user_data["other"] = other
    
    return jsonify(user_data), 200

@app.route("/create-data", methods=["POST"])
def create_data():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)