from flask import Flask, jsonify, request


app = Flask(__name__)
todos=[
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]


# mostramos nuestros datos
@app.route('/todos', methods=['GET'])
def hello_world():
    json_var= jsonify(todos)
    return json_var

# modificamos nuestros datos
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body=request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

#eliminamos datos
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("this is the position to delete:",position)
   
    todos.pop(position-1)
   
    return jsonify(todos)



if __name__== '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)