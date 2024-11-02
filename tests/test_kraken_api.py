import json
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timezone
from krakenstream import KrakenApi

class TestKrakenApi(unittest.TestCase):
    @patch('http.client.HTTPSConnection')
    def test_get_server_time(self, mock_http_connection):
        kraken = KrakenApi()
        mock_conn = mock_http_connection.return_value
        mock_response = MagicMock()
        mock_json_response = {
            "error": [],
            "result": {
                "unixtime": 1688669448,
                "rfc1123": "Thu, 06 Jul 23 18:50:48 +0000"
            }
        }
        mock_response.read.return_value = json.dumps(mock_json_response)
        mock_conn.getresponse.return_value = mock_response
        response = kraken.get_server_time()
        self.assertEqual(response, datetime(2023, 7, 6, 18, 50, 48, tzinfo=timezone.utc))

if __name__ == '__main__':
    unittest.main()
