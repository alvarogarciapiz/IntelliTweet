import unittest
from unittest.mock import patch, MagicMock
import twitter

class TestTwitter(unittest.TestCase):
    @patch('twitter.tweepy.API')
    @patch('twitter.tweepy.Client')
    def test_send_tweet(self, mock_client, mock_api):
        mock_api_instance = MagicMock()
        mock_api.return_value = mock_api_instance
        mock_api_instance.media_upload.return_value.media_id_string = "media_id"
        mock_client_instance = MagicMock()
        mock_client.return_value = mock_client_instance
        twitter.send_tweet("tweet_text", "image_path")
        mock_api_instance.media_upload.assert_called_once_with(filename="image_path")
        mock_client_instance.create_tweet.assert_called_once_with(text="tweet_text", media_ids=["media_id"])

if __name__ == '__main__':
    unittest.main()