import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):
    def test_set_mode(self):
        main.set_mode("CLASSIC")
        self.assertEqual(main.MODE, "CLASSIC")

    @patch('main.translate')
    def test_mode_decision(self, mock_translate):
        mock_translate.return_value = "a" * 273
        main.title = "title"
        main.content = "content"
        main.set_mode("AI")
        main.decide_mode()
        self.assertEqual(main.MODE, "CLASSIC")

    @patch('main.translate')
    @patch('main.create_prompt')
    @patch('main.generate_text')
    @patch('main.extract_answer')
    @patch('main.send_tweet')
    def test_ai_mode(self, mock_send_tweet, mock_extract_answer, mock_generate_text, mock_create_prompt, mock_translate):
        mock_translate.return_value = "a" * 275
        mock_create_prompt.return_value = "prompt"
        mock_generate_text.return_value = "response"
        mock_extract_answer.return_value = "answer"
        main.title = "title"
        main.content = "content"
        main.set_mode("AI")
        main.run_ai_mode()
        mock_send_tweet.assert_called_once_with("answer", "./image.jpg")

if __name__ == '__main__':
    unittest.main()