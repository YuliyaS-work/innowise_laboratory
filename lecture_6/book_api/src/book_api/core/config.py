"""
Application configuration settings.

Defines global constants such as application name, debug mode,
and database connection URL.
"""


class Settings:
    """Global application configuration settings."""
    APP_NAME: str = "book_api"
    DEBUG: bool = True
    DB_URL: str = "sqlite:///./books.db"