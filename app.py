from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/greet/<name>", methods=["GET"])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/api/data", methods=["POST"])
def create_data():
    data = request.get_json()
    return jsonify(data), 201

@app.route("/api/data/<int:data_id>", methods=["PUT"])
def update_data(data_id):
    data = request.get_json()
    return jsonify({"id": data_id, "data": data})

@app.route("/api/data/<int:data_id>", methods=["DELETE"])
def delete_data(data_id):
    return jsonify({"message": f"Data with id {data_id} has been deleted"}), 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)