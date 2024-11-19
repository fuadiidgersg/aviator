from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for the frontend

@app.route('/predict', methods=['POST'])
def predict_next_pink():
    try:
        data = request.json
        last_pink_time_str = data.get('last_pink_time')  # e.g., "2024-11-20 14:30:00"
        
        # Convert to datetime object
        last_pink_time = datetime.strptime(last_pink_time_str, "%Y-%m-%d %H:%M:%S")
        
        # Add 6 minutes to the last pink number
        next_pink_time = last_pink_time + timedelta(minutes=6)
        
        return jsonify({
            "status": "success",
            "next_pink_time": next_pink_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
