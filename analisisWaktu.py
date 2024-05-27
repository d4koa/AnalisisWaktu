from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    n = int(request.form['number'])
    start_time = time.time()
    
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
        time.sleep(0.1)  # Simulasi waktu proses, bisa disesuaikan atau dihapus
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    return jsonify(numbers=numbers, elapsed_time=elapsed_time)

if __name__ == '__main__':
    app.run(debug=True)
