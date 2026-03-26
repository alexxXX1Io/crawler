from dotenv import load_dotenv
import os

load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
print(API_HASH, "", API_ID)