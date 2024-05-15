import os
from dotenv import load_dotenv

load_dotenv()

database_key = os.getenv('DATABASE_URL')
