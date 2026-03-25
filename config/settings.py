from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="secrets.env", override=True)
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php"
USERNAME=os.getenv("USERNAME")
PASSWORD=os.getenv("PASSWORD")