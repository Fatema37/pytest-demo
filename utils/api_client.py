import requests
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"

)
logger = logging.getLogger(__name__)

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()


    def get(self, endpoint):
        url = self.base_url + endpoint
        logger.info(f"GET request to: {url}")
        response = self.session.get(url)
        logger.info(f" Response status: {response.status_code}")
        return response



    def post(self, endpoint, payload):
        url = self.base_url + endpoint
        logger.info(f"POST request to : {url}")
        response = self.session.post(url, json=payload)
        logger.info(f" Response status: {response.status_code}")
        return response


  #
  # Think about it this way — if you call requests.get() directly in every test, and tomorrow you need to:
  # - Add an auth token to every request → you'd edit 50 tests
  # - Change the base URL → edit 50 tests
  # - Add logging for every request/response → edit 50 tests
  # - Add a timeout or retry → edit 50 tests



