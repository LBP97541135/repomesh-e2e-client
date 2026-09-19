"""Flask application for displaying API health status."""

from flask import Flask, render_template_string
from src.health_status import check_health, get_api_url


app = Flask(__name__)

STATUS_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Status</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .status-card {
            background: white;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        .status-item {
            display: flex;
            justify-content: space-between;
            padding: 15px 0;
            border-bottom: 1px solid #eee;
        }
        .status-item:last-child {
            border-bottom: none;
        }
        .label {
            color: #666;
            font-weight: 500;
        }
        .value {
            color: #333;
        }
        .status-healthy {
            color: #28a745;
        }
        .status-unhealthy {
            color: #dc3545;
        }
        .status-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 4px;
            font-weight: bold;
        }
        .status-badge.healthy {
            background-color: #d4edda;
            color: #155724;
        }
        .status-badge.unhealthy {
            background-color: #f8d7da;
            color: #721c24;
        }
        .error-message {
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 4px;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="status-card">
        <h1>API Status</h1>
        
        <div class="status-item">
            <span class="label">API Endpoint</span>
            <span class="value">{{ api_url }}/healthz</span>
        </div>
        
        <div class="status-item">
            <span class="label">Status</span>
            <span class="value">
                <span class="status-badge {{ 'healthy' if health.status == 'healthy' else 'unhealthy' }}">
                    {{ health.status }}
                </span>
            </span>
        </div>
        
        <div class="status-item">
            <span class="label">Version</span>
            <span class="value">{{ health.version }}</span>
        </div>
        
        {% if health.error %}
        <div class="error-message">
            <strong>Error:</strong> {{ health.error }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    """Display the health status page."""
    health = check_health()
    return render_template_string(
        STATUS_PAGE_TEMPLATE,
        health=health,
        api_url=get_api_url()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
