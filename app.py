from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "<h1>Witaj w aplikacji zadania!</h1><p>Użyj /tasks, aby zarządzać zadaniami.</p>"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Podaj poprawne dane!"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "done": False
    }
    tasks.append(new_task)
    return jsonify({"message": "Dodano zadanie!", "task": new_task}), 201

if __name__ == '__main__':
    app.run(debug=True)
