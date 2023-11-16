import unittest
from unittest.mock import patch, MagicMock
import utils

class TestUtils(unittest.TestCase):
    def test_transform_url_imore(self):
        url = "http://example.com/320-80.jpg"
        expected_url = "http://example.com/650-80.jpg"
        self.assertEqual(utils.transform_url_imore(url), expected_url)

    @patch('utils.os.remove')
    def test_delete_image(self, mock_remove):
        utils.delete_image("image_path")
        mock_remove.assert_called_once_with("image_path")

    @patch('utils.requests.get')
    def test_download_image(self, mock_get):
        mock_response = MagicMock()
        mock_get.return_value = mock_response
        mock_response.iter_content.return_value = [b"chunk1", b"chunk2"]
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            utils.download_image("image_url", "file_path")
            mock_get.assert_called_once_with("image_url", stream=True)
            mock_file().write.assert_any_call(b"chunk1")
            mock_file().write.assert_any_call(b"chunk2")

    def test_extract_answer(self):
        response = MagicMock()
        response.text = json.dumps({"response": json.dumps({"message": "answer"})})
        self.assertEqual(utils.extract_answer(response), "answer")

if __name__ == '__main__':
    unittest.main()