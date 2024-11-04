from crossmint_challenge.api import MegaverseAdapter
from unittest.mock import patch, Mock
import unittest

megaverse_content = [[{"type": 0}, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [
    None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None]]


class TestMegaverseAdapter(unittest.TestCase):

    @patch('crossmint_challenge.api.requests.get')
    def test_fetch_map_success(self, mock_get):
        candidate_id = "test_candidate_id"
        adapter = MegaverseAdapter(candidate_id)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "map": {
                "content": megaverse_content
            }
        }
        mock_get.return_value = mock_response

        resp = adapter.fetch_map()

        self.assertEqual(resp, megaverse_content)

    @patch('crossmint_challenge.api.requests.get')
    def test_fetch_map_failure(self, mock_get):
        candidate_id = "test_candidate_id"
        adapter = MegaverseAdapter(candidate_id)
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        resp = adapter.fetch_map()

        self.assertListEqual(resp, [[]])


if __name__ == '__main__':
    unittest.main()
