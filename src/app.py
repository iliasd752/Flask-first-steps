from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
{
    "label": "My first task",
    "done": False
},
{
    "label": "My second task",
    "done": False
}
]


@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the index position to delete: ", position)
    return jsonify(todos)




# pipenv run python src/app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)