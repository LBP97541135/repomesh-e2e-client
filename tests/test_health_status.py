"""Tests for health status module."""

import unittest
from unittest.mock import patch, MagicMock
from src.health_status import check_health, get_api_url, HealthStatus


class HealthStatusTest(unittest.TestCase):
    @patch("src.health_status.urlopen")
    def test_check_health_success(self, mock_urlopen):
        """Test successful health check response."""
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"status": "healthy", "version": "1.0.0"}'
        mock_urlopen.return_value.__enter__.return_value = mock_response
        
        result = check_health()
        
        self.assertEqual(result.status, "healthy")
        self.assertEqual(result.version, "1.0.0")
        self.assertEqual(result.error, "")

    @patch("src.health_status.urlopen")
    def test_check_health_unhealthy(self, mock_urlopen):
        """Test unhealthy API response."""
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"status": "unhealthy"}'
        mock_urlopen.return_value.__enter__.return_value = mock_response
        
        result = check_health()
        
        self.assertEqual(result.status, "unhealthy")

    @patch("src.health_status.urlopen")
    def test_check_health_url_error(self, mock_urlopen):
        """Test URL error handling."""
        from urllib.error import URLError
        mock_urlopen.side_effect = URLError("Connection refused")
        
        result = check_health()
        
        self.assertEqual(result.status, "unhealthy")
        self.assertIn("Connection refused", result.error)

    @patch("src.health_status.urlopen")
    def test_check_health_json_error(self, mock_urlopen):
        """Test JSON decode error handling."""
        mock_response = MagicMock()
        mock_response.read.return_value = b"not valid json"
        mock_urlopen.return_value.__enter__.return_value = mock_response
        
        result = check_health()
        
        self.assertEqual(result.status, "unhealthy")
        self.assertIn("Invalid JSON", result.error)

    def test_get_api_url_default(self):
        """Test default API URL."""
        with patch.dict("os.environ", {}, clear=True):
            url = get_api_url()
            self.assertEqual(url, "http://localhost:8080")

    def test_get_api_url_from_env(self):
        """Test API URL from environment variable."""
        with patch.dict("os.environ", {"API_BASE_URL": "http://custom-api:9000"}):
            url = get_api_url()
            self.assertEqual(url, "http://custom-api:9000")


if __name__ == "__main__":
    unittest.main()
