import unittest
from unittest.mock import patch, MagicMock
import scraper

class TestScraper(unittest.TestCase):
    @patch('scraper.webdriver.Firefox')
    def test_macrumors(self, mock_firefox):
        mock_driver = MagicMock()
        mock_firefox.return_value = mock_driver
        mock_driver.page_source = "<html></html>"
        mock_soup = MagicMock()
        scraper.BeautifulSoup = MagicMock(return_value=mock_soup)
        mock_soup.find.return_value.text = "text"
        mock_soup.select.return_value = [{"srcset": "image_url 100w"}]
        result = scraper.scrape("https://www.macrumors.com")
        self.assertEqual(result, {"title": "text", "image_url": "image_url", "content": "text"})

    # Similar tests for '9to5mac' and 'imore' would go here

if __name__ == '__main__':
    unittest.main()