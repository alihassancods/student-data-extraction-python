from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
load_dotenv()
URL_ENDPOINT = str(os.getenv("URL_ENDPOINT"))
