import unittest
import gcshus
from google.cloud import storage
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.


class TestSignedURL(unittest.TestCase):
    def test_generate_download_signed_url(self):
        url = gcshus.generate_download_signed_url(
            storage.Client(), os.environ["TEST_GCS_BUCKET"], "test.txt", 5
        )
        assert len(url) > 0

    def test_generate_download_signed_url_with_token_refresh(self):
        url = gcshus.generate_download_signed_url_with_token_refresh(
            storage.Client(), os.environ["TEST_GCS_BUCKET"], "test.txt", 5
        )
        assert len(url) > 0


if __name__ == "__main__":
    unittest.main()
