import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_host = os.getenv('POSTGRES_HOST')
postgres_port = os.getenv('POSTGRES_PORT')
postgres_db = os.getenv('POSTGRES_DB')

# Use the retrieved values to construct the connection string or configure your database connection accordingly


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL')
