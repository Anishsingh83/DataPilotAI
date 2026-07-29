import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY")

    DEBUG = os.getenv("DEBUG", "False") == "True"

    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 5000))

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///instance/database.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Upload Folder
    UPLOAD_FOLDER = "uploads"

    # Allowed File Extensions
    ALLOWED_EXTENSIONS = {"csv", "xlsx", "json"}
    
    