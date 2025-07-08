from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/api/cloud-data')
def get_cloud_data():
    """Endpoint to fetch cloud cluster data"""
    # Generate mock data - in a real app this would come from INSAT data processing
    data = {
        "last_updated": datetime.utcnow().isoformat(),
        "total_clusters": random.randint(50, 150),
        "developing_clusters": random.randint(5, 30),
        "intense_clusters": random.randint(5, 20),
        "avg_size_km": random.randint(50, 200),
        "temperature_profile": [random.randint(-70, -50) for _ in range(8)],
        "size_distribution": [random.randint(5, 50) for _ in range(5)],
        "recent_clusters": [
            {
                "id": f"CLD-{random.randint(1000, 9999)}",
                "region": random.choice(["Bay of Bengal", "Arabian Sea", "South Indian Ocean"]),
                "detected": (datetime.utcnow().timestamp() - random.randint(60, 14400)),
                "status": random.choice(["Developing", "Mature", "Dissipating"]),
                "size_km": random.randint(50, 300),
                "min_temp": random.randint(-70, -50)
            } for _ in range(6)
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
