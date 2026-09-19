"""Health status module for checking API health endpoint."""

import os
from dataclasses import dataclass
from urllib.request import urlopen
from urllib.error import URLError
import json


@dataclass
class HealthStatus:
    """Health status response from API."""
    status: str
    version: str = ""
    error: str = ""


def get_api_url() -> str:
    """Get API URL from environment variable or use default."""
    return os.environ.get("API_BASE_URL", "http://localhost:8080")


def check_health() -> HealthStatus:
    """Check the health status of the API endpoint."""
    api_url = get_api_url()
    health_endpoint = f"{api_url}/healthz"
    
    try:
        with urlopen(health_endpoint, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))
            return HealthStatus(
                status=data.get("status", "unknown"),
                version=data.get("version", "unknown")
            )
    except URLError as e:
        return HealthStatus(
            status="unhealthy",
            error=str(e)
        )
    except json.JSONDecodeError:
        return HealthStatus(
            status="unhealthy",
            error="Invalid JSON response"
        )
    except Exception as e:
        return HealthStatus(
            status="unhealthy", 
            error=str(e)
        )
