from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample tasks (simulating Jenkins jobs)
tasks = {
    "build": "pending",
    "test": "pending",
}

@app.route('/')
def home():
    """Home page of the web server."""
    return "Welcome to the Simple Web Server!", 200

@app.route('/status', methods=['GET'])
def status():
    """Check server status."""
    return jsonify({"status": "running", "tasks": tasks}), 200

@app.route('/start_task/<task_name>', methods=['POST'])
def start_task(task_name):
    """Start a specified task."""
    if task_name in tasks:
        tasks[task_name] = "running"
        return jsonify({"message": f"{task_name} started"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route('/stop_task/<task_name>', methods=['POST'])
def stop_task(task_name):
    """Stop a specified task."""
    if task_name in tasks:
        tasks[task_name] = "stopped"
        return jsonify({"message": f"{task_name} stopped"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route('/task_status/<task_name>', methods=['GET'])
def task_status(task_name):
    """Check the status of a specific task."""
    if task_name in tasks:
        return jsonify({task_name: tasks[task_name]}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
